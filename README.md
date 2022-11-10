
How to make a curl request, based on the test example:

curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"seatsGrid": [[3,2], [4,3], [2,3], [3,4]] , "passengers": 30}' \
    http://localhost:5000/airplane-algo

The response will be of form 

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