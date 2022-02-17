# sdk-python

PythonSDK to access Bauction on the internet computer

# Installation:

You'll need ic-py module to use sdk. First git clone sdk-python repo. cd into it & then run:

```
git clone git@github.com:rocklabs-io/ic-py.git
cd ic-py
pip3 install ./
```

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
