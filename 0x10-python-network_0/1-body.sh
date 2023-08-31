#!/bin/bash
#  takes in a URL, sends a GET request to the URL, and displays the body of the response with 200 status code response
curl -sL "$1"
