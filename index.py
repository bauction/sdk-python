from datetime import datetime
from ic.client import Client
from ic.identity import Identity
from ic.candid import encode, Types
from ic.agent import Agent
from bauctionIDL import IDL

class Bauction:
    def __init__(self, pem, host="https://ic0.app"):
        self.pem=pem
        self.host=host
        self.identity=Identity.from_pem(pem)
        self.client=Client(host)
        self.agent=Agent(self.identity, self.client)
        self.canisterId="rrkah-fqaaa-aaaaa-aaaaq-cai"

    def getIdentity(self):
        return self.identity.sender()
    
    def createProfile(self, name, location, about):
        record=Types.Record({
            'name': Types.Text,
            'location': Types.Text,
            'about': Types.Text
        })

        params=[
            {
                'type': record,
                'value': {
                    'name': name,
                    'location': location,
                    'about': about
                }
            }
        ]
        return self.agent.update_raw(self.canisterId, "createProfile", encode(params), IDL["createProfile"])
    
    def getMyProfile(self):
        return self.agent.update_raw(self.canisterId, "getProfile", encode([]), IDL["getMyProfile"])
    
    def updateMyProfile(self, name, location, about):
        bioRecord=Types.Record({
            'name': Types.Text,
            'location': Types.Text,
            'about': Types.Text
        })
        record=Types.Record({
            'bio': bioRecord
        })
        params=[
            {
                'type': record,
                'value': {
                    'bio': {
                        'name': name,
                        'location': location,
                        'about': about
                    }
                }
            }
        ]
        return self.agent.update_raw(self.canisterId, "updateProfile", encode(params), IDL["updateMyProfile"])
    
    def deleteMyProfile(self):
        return self.agent.update_raw(self.canisterId, "deleteProfile", encode([]), IDL["deleteMyProfile"])
    
    def getProfileById(self, sellerId):
        params=[{'type': Types.Text, 'value': sellerId}]
        return self.agent.query_raw(self.canisterId, "getProfileById", encode(params), IDL.getProfileById)
    
    def createAuction(self, name, startDate, endDate, description, minBidAmt, maxBidAmt, category, location, auctionType):
        AuctionTypeRecord=Types.Variant({
            auctionType: Types.Null
        })
        record=Types.Record({
            'name': Types.Text,
            'startDate': Types.Text,
            'endDate': Types.Text,
            'description': Types.Text,
            'minBidAmt': Types.Nat,
            'maxBidAmt': Types.Nat,
            'category': Types.Text,
            'location': Types.Text,
            'auctionType': AuctionTypeRecord
        })

        params=[
            {
                'type': record,
                'value': {
                    'name': name,
                    'startDate': startDate,
                    'endDate': endDate,
                    'description': description,
                    'minBidAmt': minBidAmt,
                    'maxBidAmt': maxBidAmt,
                    'category': category,
                    'location': location,
                    'auctionType': {
                        auctionType: None
                    }
                }
            }
        ]
        return self.agent.update_raw(self.canisterId, "createAuction", encode(params), IDL["createAuction"])

    def updateAuction(self, auctionId, name, description):
        AuctionTypeRecord=Types.Variant({
            'ForwardAuction': Types.Null
        })
        record=Types.Record({
            'name': Types.Text,
            'startDate': Types.Text,
            'endDate': Types.Text,
            'description': Types.Text,
            'minBidAmt': Types.Nat,
            'maxBidAmt': Types.Nat,
            'category': Types.Text,
            'location': Types.Text,
            'auctionType': AuctionTypeRecord
        })

        params=[
            {
                'type': record,
                'value': {
                    'name': name,
                    'startDate': "",
                    'endDate': "",
                    'description': description,
                    'minBidAmt': 0,
                    'maxBidAmt': 0,
                    'category': "general",
                    'location': "",
                    'auctionType': {
                        'ForwardAuction': None
                    }
                }
            }
        ]
        return self.agent.update_raw(self.canisterId, "updateAuction", encode(params), IDL["updateAuction"])


    def deleteAuction(self):
        return self.agent.update_raw(self.canisterId, "deleteProfile", encode([]), IDL["updateAuction"])
    
    def getMyAuctions(self):
        return self.agent.update_raw(self.canisterId, "getMyAuctions", encode([]), IDL["getMyAuctions"])[0]["value"]

    def getAllAuctions(self):
        return self.agent.query_raw(self.canisterId, "getAllAuctions", encode([]), IDL["getAllAuctions"])[0]["value"]

    def getAuctionsBySellerId(self, sellerId):
        params=[{'type': Types.Text, 'value': sellerId}]
        return self.agent.query_raw(self.canisterId, "getAuctionBySellerId", encode(params), IDL["getAuctionsBySellerId"])

    def getMyAuctionCount(self):
        return self.agent.update_raw(self.canisterId, "getMyAuctionCount", encode([]), IDL["getMyAuctionCount"])

    def findAuctionById(self, auctionId):
        params=[{'type': Types.Text, 'value': auctionId}]
        return self.agent.query_raw(self.canisterId, "findAuction", encode(params), IDL["findAuctionById"])

    def getAuctionWinner(self, auctionId):
        params=[{'type': Types.Text, 'value': auctionId}]
        return self.agent.query_raw(self.canisterId, "getWinner", encode(params), IDL["getAuctionWinner"])

    def getHighestBid(self, auctionId):
        params=[{'type': Types.Text, 'value': auctionId}]
        return self.agent.update_raw(self.canisterId, "getHighestBid", encode(params), IDL["getHighestBid"])

    def bidOnAuction(self, auctionId, bidAmount):
        params=[
            {
                'type': Types.Text,
                'value': auctionId
            },
            {
                'type': Types.Nat,
                'value': bidAmount
            },
            {
                'type': Types.Text,
                'value': str(datetime.utcnow())
            }
        ]
        return self.agent.update_raw(self.canisterId, "bidOnAuction", encode(params), IDL["bidOnAuction"])