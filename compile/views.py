from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from urllib.parse import urlparse
# from urlparse import urlparse

# for sending requests and parsing response
import requests
from bs4 import BeautifulSoup

# for extracting keywords from error messages
from rake_nltk import Rake


# Constants
RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
CLIENT_SECRET = '41662da152e210d7610787a8596e45cda8638dde'


def get_domain(url):
    """
    Parameters:
    url[string] => uniform resource locator of website
    --------------------------------------------
    Returns:
    parsed_uri.netloc [string] => the domain name in url
    Logic:
    Given a url return its domain
    """

    parsed_uri = urlparse(url)
    return(parsed_uri.netloc)


def compiler(request):
    return render(request, 'compiler.html')


def codeplay(request):
    """
    Parameters:
    request[HttpRequest]
    --------------------------------------------
    Returns:
    render(request, 'codeplay.html') [HttpResponse]
                => codeplay.html is returned as HttpResponse
    Logic:
    re-renders the codeplay page
    """

    return render(request, 'codeplay.html')
