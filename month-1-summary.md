# Month 1 Summary

### Question

Which settlements in Akure South LGA are located within 200 m of mapped watercourses?

### Operation and why

I reprojected the watercourse data to UTM Zone 31N and clipped the watercourses to the Akure South study area. I then created a **200 m buffer around the clipped watercourses without dissolving the features**. The buffer was used to define the zone surrounding the mapped watercourses and provide the first step towards identifying settlements that are near them.

### What I expected and what I got

I expected the clipped watercourse layer to contain 30 features and therefore expected the undissolved buffer to contain 30 features. The buffer produced **30 features**, matching the clipped input.

A manual measurement from a watercourse to the buffer edge gave **about 198 m**, which is close to the intended 200 m distance.

The reprojected watercourse layer contained **54 features**, while the clipped layer contained 30. The 24 features removed during clipping were outside the study area and did not intersect the clipped extent.

### What surprised me

The clipped dataset contained **15 watercourse features tagged as `tunnel = culvert`**. These are piped sections carrying water beneath roads, but they are still included in the watercourse network and therefore in the 200 m buffer. A follow-up spatial join returned one large settlement polygon rather than a useful settlement-level proximity result, so the settlement data require further examination before they can be used reliably for a simple near/not-near assessment.

### What data I still need

I still need **elevation data and more detailed settlement data** to assess whether settlements within the buffer are actually exposed to low-lying or flood-prone conditions. The 200 m buffer only defines spatial proximity to mapped watercourses and is not, by itself, a flood-risk assessment.
