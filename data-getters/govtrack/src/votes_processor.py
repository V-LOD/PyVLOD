import constants as c

def process_votes(votes, bill_uri):
    # return an array of (Voter reactsTo Bill) triples, generated from the given bill uri and vote data

    def vote_triple(voter_id, k): return ('<gt_v/%s>' % voter_id, c.VOTE_VOC[k], bill_uri)
    def is_dict(thing): return isinstance(thing,dict)

    triples = []
    for k in c.VOTE_VOC.keys():
        if k in votes: triples += [vote_triple(v['id'],k) for v in votes[k] if is_dict(v)]
    return triples