from ic.candid import Types

List=Types.Rec()
List__1=Types.Rec()
AuctionDirectionType=Types.Variant({
    'ETender': Types.Null,
    'ForwardAuction': Types.Null,
    'ReverseAuction': Types.Null,
    'FlexibleOffers': Types.Null,
})

AuctionInput=Types.Record({
    'maxBidAmt': Types.Nat,
    'endDate': Types.Text,
    'auctionType': AuctionDirectionType,
    'minBidAmt': Types.Nat,
    'name': Types.Text,
    'description': Types.Text,
    'category': Types.Text,
    'location': Types.Text,
    'startDate': Types.Text,
})

UserId=Types.Principal
Bid=Types.Record({
    'id': UserId,
    'bid': Types.Nat,
    'submittedAt': Types.Text
})

List.fill(Types.Opt(Types.Tuple(Bid, List)))

AuctionResponse=Types.Record({
    'id': Types.Text,
    'status': Types.Bool,
    'maxBidAmt': Types.Nat,
    'endDate': Types.Text,
    'auctionType': AuctionDirectionType,
    'minBidAmt': Types.Nat,
    'bids': List,
    'name': Types.Text,
    'createdBy': Types.Text,
    'description': Types.Text,
    'currency': Types.Text,
    'category': Types.Text,
    'location': Types.Text,
    'startDate': Types.Text,
})

Bio = Types.Record({
    'about': Types.Text,
    'name': Types.Text,
    'location': Types.Text,
})

Error=Types.Variant({
    'NotFound': Types.Null,
    'NotAuthorized': Types.Null,
    'AlreadyExists': Types.Null
})

Result=Types.Variant({'ok': Types.Null, 'err': Error})
AuctionType=Types.Record({
    'id': Types.Text,
    'maxBidAmt': Types.Nat,
    'endDate': Types.Text,
    'auctionType': AuctionDirectionType,
    'minBidAmt': Types.Nat,
    'bids': List,
    'name': Types.Text,
    'createdBy': Types.Principal,
    'description': Types.Text,
    'currency': Types.Text,
    'category': Types.Text,
    'location': Types.Text,
    'photos': List,
    'startDate': Types.Text,
})
List__1.fill(Types.Opt(Types.Tuple(AuctionInput, List__1)))
Result_3 = Types.Variant({ 'ok': List__1, 'err': Error })
Result_4=Types.Variant({'ok': Types.Nat, 'err': Error})
Profile=Types.Record({'id': Types.Principal, 'bio': Bio})
Result_2=Types.Variant({'ok': Profile, 'err': Error})
Result_1 = Types.Variant({'ok': AuctionResponse, 'err': Error})
ProfileUpdate = Types.Record({'bio': Bio})

IDL={
    'bioOnAuction': Types.Bool,
    'convertPrincipalToText': Types.Text,
    'createAuction': Types.Opt(AuctionResponse),
    'createProfile': Result,
    'deleteAuction': Result,
    'deleteProfile': Result,
    'findAuction': Types.Opt(AuctionType),
    'getAllAuctions': Result_3,
    'getAuctionBySellerId': Result_3,
    'getHighestBid': Types.Nat,
    'getMyAuctionCount': Result_4,
    'getMyAuctions': Result_3,
    'getMyIdentity': Types.Text,
    'getProfile': Result_2,
    'getProfileById': Result_2,
    'getProfileByPrincipalId': Result_2,
    'getWinner': Types.Text,
    'healthcheck': Types.Bool,
    'updateAuction': Result_1,
    'updateProfile': ProfileUpdate,
}