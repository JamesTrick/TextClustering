# Clustering Email Responses To Identify Similar Responses

Within an Email Support an environment, knowledge is stored in knowledge articles. These articles are typically created on an as-needed basis and then attached as emails come through. Due
to way Knowledge Articles are created, there is a heavy importance on agents reporting and suggesting new articles. However, for agents there is a constant trade-off between doing cases
and reporting what's needed. Consequently, we have a number of large KAs that have a high case count but are considered a 'catch-all'. From a reporting perspective, these KAs likely dominate
reports despite haing little value.

This repo focuses on using a Clustering Algorithm on these large KAs to see if there are potential segments within the KAs that we can split into new KAs for better reporting and for faster
resoultion times of cases by having a dedicated KA and template. Depending on the volumes of the segmentted KA, there may be the possibililty of automating responses to it as well.

# About Clustering

Clustering is a machine learning technique that groups objects into clusters based of how similar they are compared to other clusters. It's an unsupervised learning technique which means
we don't need to input labelled data such as we've done in the Auto-answer analysis - this saves money in terms of labour required to label data.

# Contents of this repo

The Clustering Example notebook runs through an example of Clustering using data from two news websites and explores clustering to highlight the value of clustering and give insight as to how clustering could be used within a Customer Support environment.
