import numpy as np

totalEmails = 1000
nonSpamEmails = 600
spamEmails = 400
offerNonSpam = 480
offerSpam = 360

pSpam = spamEmails / totalEmails
pOfferGivenSpam = offerSpam / spamEmails
pOffer = (offerSpam + offerNonSpam) / totalEmails

pSpamGivenOffer = np.round((pOfferGivenSpam * pSpam) / pOffer, 4)

print("The probability that an email is spam given that it contains the word 'offer' is:", pSpamGivenOffer)