
# Airplane Seating Algorithm API

## Steps to run

1. Run the following command:
```
python server.py
```

2. On a parallel terminal tab, run the curl request
```
curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"seatsGrid": [[3,2], [4,3], [2,3], [3,4]] , "passengers": 30}' \
    http://localhost:5000/airplane-algo
```

The response will be of form 
```
{
  "arrangement": [
    [
      [ 19, 25, 1],
      [ 21, 29, 7]
    ],
    [
      [ 2, 26, 27, 3 ],
      [ 8, 30, -1, 9 ],
      [ 13, -1, -1, 14 ]
    ],
    [
      [ 4, 5 ],
      [ 10, 11 ],
      [ 15, 16 ]
    ],
    [
      [ 6, 28, 20 ],
      [ 12, 31, 22 ],
      [ 17, -1, 23 ],
      [ 18, -1, 24 ]
    ]
  ]
}
```

To test the code on Postman:
1. Run server.py
2. On the request URL input, enter the following, and set the request header to POST:
```
http://localhost:5000/airplane-algo
```
3. On the Body tab, enter the following JSON text
```
{
    "seatsGrid": [[3,2], [4,3], [2,3], [3,4]],
    "passengers": 30
}
```
4. Make the request.

The output will be same as above.
