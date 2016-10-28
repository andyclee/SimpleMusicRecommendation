## Simple Music Recommendation
# Uses Wikipedia, Spotify, and Twitter APIs

| Method | Endpoint          | Usage                                               | Returns   |
|--------|-------------------|-----------------------------------------------------|-----------|
| GET    | /twitter/<queryT> | Get tweets about a given query                      | JSON file |
| GET    | /wiki/<queryW>    | Get the wikipedia article summary for a given query | JSON file |
| GET    | /spotify/<queryS> | Get the top tracks for a given query                | JSON file |
| GET    | /rec/<queryG>     | Gets recommended tracks from Spotify                | JSON file |