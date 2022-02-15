# sdk-python

PythonSDK to access Bauction on the internet computer

```py
from Bauction import Bauction

pemString="-----BEGIN PRIVATE KEY-----\n YOUR SECRET KEY \n-----END PRIVATE KEY-----"
#create instance of bauction
instance = Bauction(pemString, host)
#host is optional here. Default host is "https://ic0.app".
allAuctions = instance.getMyAuctions() #returns auctions of authenticated user.
```

# Other available methods:

- createProfile
- getMyProfile
- updateMyProfile
- deleteMyProfile
- updateAuction
- deleteAuction
- getMyAuctions
- getAllAuctions
- getAuctionsBySellerId
- getMyAuctionCount
- findAuctionById
- getAuctionWinner
- getHighestBid
- bidOnAuction
