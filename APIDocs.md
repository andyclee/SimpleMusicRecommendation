# Simple Music Recommendation
## Uses Wikipedia, Spotify, and Twitter APIs

| Method | Endpoint          | Request Parameter | Usage                                               | Returns   |
|--------|-------------------|-------------------|-----------------------------------------------------|-----------|
| GET    | /twitter/<queryT> | queryT            | Get tweets about a given query                      | JSON file |
| GET    | /wiki/<queryW>    | queryW            | Get the wikipedia article summary for a given query | JSON file |
| GET    | /spotify/<queryS> | queryS            | Get the top tracks for a given query                | JSON file |
| GET    | /rec/<queryG>     | queryG            | Gets recommended tracks from Spotify                | JSON file |
