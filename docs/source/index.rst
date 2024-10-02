.. Theoretical Market Framework documentation master file, created by
   sphinx-quickstart on Thu Oct  1 20:41:40 2023.

Welcome to Theoretical Market Framework's documentation!
====================================

.. Contents:
---------

.. toctree::
    :maxdepth: 2
    :caption: Contents

    README.md  # Ensure this line points to your README.md file

.. include:: ../README.md  # Include content from README.md located at the root

---------
.. toctree::
   :maxdepth: 2
   .. :caption: Table of Contents

   .. theoretical_market_framework

Theoretical Market Framework
=============================

The Theoretical Market Framework (TMF) is proposed to analyze existing markets and guide the design and integration of new markets for procuring system services. The TMF helps describe the market architecture through a set of pillars, features, and sub-features, while identifying the corresponding design options. 

The TMF comprises five pillars, each with distinct characteristics: (i) overall market architecture, (ii) sub-market coordination, (iii) market optimization, (iv) market operation, and (v) network representation. Some attributes apply across the entire market, explaining sub-market coordination, while others are specific to individual sub-markets. A thorough market design and analysis requires systematically evaluating each pillar and its corresponding attributes for each feature or sub-feature.

.. image:: images/TMF_00_All_Pillars.svg
   :alt: Theoretical Market Framework overview
   :align: center


Market architecture pillar
---------------------------

The 'market architecture' pillar encompasses the features that define the overarching characteristics of the market structure as a whole.
.. image:: images/TMF_01_Architecture.svg
   :alt: Market architecture pillar
   :align: center



Sub-market coordination pillar
-------------------------------

The 'Sub-market coordination' pillar includes features that describe how sub-markets interact, particularly in relation to the allocation of shared resources.
.. image:: images/TMF_02_Coord.svg
   :alt: Sub-market coordination pillar
   :align: center


Market optimization pillar
---------------------------

The ‘Market Optimization’ pillar encompasses the features that determine how a sub-market is cleared and how this clearing process interacts with other sub-markets within the overall market architecture.
.. image:: images/TMF_03_Opt.svg
   :alt: Market optimization pillar
   :align: center


Market operation pillar
-----------------------

The ‘Market Operation’ pillar outlines the features that detail the operational aspects of each sub-market.
.. image:: images/TMF_04_Ope.svg
   :alt: Market operation pillar
   :align: center


Network representation pillar
-------------------------------

The ‘Network Representation’ pillar addresses the properties of the market architecture that specify how and when the network representation is taken into account.
.. image:: images/TMF_05_Net.svg
   :alt: Network representation pillar
   :align: center


References
==========

- Troncia, M., Chaves Ávila, J. P., Damas Silva, C., Gerard, H., & Willeghems, G. (2023). *Market-Based TSO–DSO Coordination: A Comprehensive Theoretical Market Framework and Lessons from Real-World Implementations*. *Energies*, 16(19), 6939. [https://doi.org/10.3390/en16196939](https://www.mdpi.com/1996-1073/16/19/6939)
- Troncia, M., Bindu, S., Chaves Ávila, J. P., Willeghems, G., Gerard, H., & Lacerda, M. (2023). *OneNet Deliverable D11.2 - Techno-economic assessment of proposed market schemes for standardized products D11.2*. [OneNet Deliverable D11.2](https://www.onenet-project.eu/wp-content/uploads/2024/01/OneNet_D11.2_V1.0.pdf)
- Chaves Ávila, J. P., Troncia, M., Silva, C. D., & Willeghems, G. (2021). *OneNet Deliverable D3.1 - Overview of market designs for the procurement of system services by DSOs and TSOs*. [OneNet Deliverable D3.1](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5df2250db&appId=PPGMS)
