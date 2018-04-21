
# coding: utf-8

# In[1]:


from bitcoin import *
import pickle
from pprint import pprint


# ## Block containing Transactions

# In[1]:


block = {
    "Transactions": [
        {
            "From" : 'A',
            "To" : 'B',
            "Amount" : 50
        },
        {
            "From" : 'B',
            "To" : 'C',
            "Amount" : 40
        },
        {
            "From" : 'C',
            "To" : 'D',
            "Amount" : 10
        }
    ]
}


# ## Signing and Verification of Block

# In[3]:


# defining some private and public keys
# For signing and authentication
priv = random_key();
pub = privtopub(priv);

# Sign the block

sign = ecdsa_sign(pickle.dumps(block), priv);


# Verfying the block

print(ecdsa_verify(pickle.dumps(block), sign, pub))


# ## Adding Additional fields to block

# In[4]:


#Adding Signature to block
block["sign"] = sign;
#Adding nonce
block["nonce"] = 0;
#Adding prev_block address
block["prev_hash"] = sha256(random_key())


# ## Defining a difficulty string

# In[5]:


difficulty = 3;
difficulty_string = ''.join(['0' for x in range(difficulty)])


# ## Mining

# In[11]:


# Mining
nonce=0
block["nonce"]=nonce
h = sha256(pickle.dumps(block))
print(block["nonce"], h)
while h[:difficulty] != difficulty_string:
    nonce +=1
    block["nonce"]=nonce
    h = sha256(pickle.dumps(block))
    print(nonce, h)


# ## Result

# In[10]:


print(nonce, h)

