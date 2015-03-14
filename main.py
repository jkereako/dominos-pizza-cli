#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# An example script using the boilerplate, to accompany the slideshow
# at <http://www.slideshare.net/saniac/the-bones-of-a-nice-python-script>.


# By using env, we'll get whatever python is on the user's path.
# Note: on some rare Unixes env is in /bin .

# The magic comment afterwards lets us put literal Unicode in our script.
# - see http://www.python.org/dev/peps/pep-0263/

# These imports support the boilerplate.
import sys
import re
from dominospizza import web_service, urls
import argparse

import random

def scramble(word):
    """
    Takes a word, and returns a scrambled version if it is longer than 3 chars.

    Scrambling preserves the first and last characters.

    >>> scramble('a')
    'a'
    >>> scramble('an')
    'an'
    >>> scramble('the')
    'the'
    >>> scramble('cart') in ['cart', 'crat']
    True
    """
    if len(word) < 4:
        return word
    innards = list(word[1:-1])
    random.shuffle(innards)
    return word[0] + ''.join(innards) + word[-1]

# From here onwards, the code comprises (modified) boilerplate.
# It is inspired by the article here:
#  <http://www.artima.com/forums/flat.jsp?forum=106&thread=4829>
# and subsequent commentary.

def _test(verbose=False):
    import doctest
    doctest.testmod(verbose=verbose)

def _profile_main(filename=None):
    import cProfile, pstats
    prof = cProfile.Profile()
    ctx = """_main(filename)"""
    prof = prof.runctx(ctx, globals(), locals())
    stats = pstats.Stats(prof)
    stats.sort_stats("time")
    stats.print_stats(10)

def _blurt(s, f):
    pass

def _main(filename=None):
    f = sys.stdin
    if filename:
        _blurt("Reading from %s", filename)
        try:
            f = file(filename)
        except Exception, ex:
            print "Couldn't open file %s: %s" % (filename, ex)
            return 1

    while 1:
        line = f.readline()
        if not line:
            break
        _blurt("Original line was: %s", line)
        sys.stdout.write(' '.join([scramble(w) for w in line.split()]) + '\n')
    return 0

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Search for Dominos locations near you.')

    parser.add_argument('street_name', metavar='street', nargs='+',
                       help='Your street name')

    parser.add_argument('zip_code', metavar='zip', nargs='+',
                       help='Your zip code')

    args = parser.parse_args()

    # Simple zip code validation
    m = re.match(r'^\d{5}(?:[-\s]\d{4})?$', args.zip_code[0])
    if m is None:
        exit('Invalid zip code')

    # TEST
    req = web_service.GetRequest(urls.store_locator_url(),{'c':args.zip_code[0],
        's':' '.join(args.street_name)})
    req.make_request()
    exit()
    #TEST

    usage = "usage: %prog [options] [filename]"
    parser = OptionParser(usage=usage)
    parser.add_option('--profile', '-P',
                       help    = "Print out profiling stats",
                       action  = 'store_true')
    parser.add_option('--test', '-t',
                       help   ='Run doctests',
                       action = 'store_true')
    parser.add_option('--verbose', '-v',
                       help   ='print debugging output',
                       action = 'store_true')

    (options, args) = parser.parse_args()

    if options.verbose:
        def really_blurt(s, f=()):
            sys.stderr.write(s % f + '\n')
        _blurt = really_blurt

    # Assign non-flag arguments here.
    filename = None

    if len(args) > 0:
        filename = args[0]
        _blurt("filename is %s", filename)

    if options.profile:
        _profile_main(filename)
        exit()

    if options.test:
        _test(verbose=options.verbose)
        exit()

    sys.exit(_main(filename))
