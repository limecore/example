limecore: Example
=================

limecore is a set of libraries that provide a flexible, rapid application-development
framework. limecore has a strongly-opinionated API, but leverages Dependency Injection
to allow the implementation of components to be replaced as necessary.

limecore Overview
-----------------

An an abstract limecore application is structured as follows:

.. code-block::

                 +----------+      +-----+
             +-> | Web API  | -+-> | DB  | -+
   +------+  |   +----------+  |   +-----+  |   +----------+
   | User | -+                 |            +-> | Services |+
   +------+  |   +----------+  |   +-----+  |   +----------+|+      +------------------+
             +-> | CLI Tool | -+-> | ESB | -+    +----------+| ---> | External Service |
                 +----------+      +-----+        +----------+      +------------------+

A user can interact with the application through a Web API (e.g., typical user), or CLI
tooling (e.g., systems administrator).

The Web API, or CLI, implement Command Query Responsibility Segregation (CQRS), and
fulfil read requests by drawing data directly from (one of) the system database(s), and
write by publishing commands onto the underlying Enterprise Service Bus (ESB).

The ESB is responsible for routing commands to the appropriate backend Service.

A backend Service responds to Commands, and may interact with one-or-more external
systems, update (one of) the system database(s), or publish further messages on the ESB
for other services (or itself) to handle later.

Running the Example
-------------------

To install dependencies:

.. code-block:: bash

   pip install -r requirements.txt

To run the Backend service:

.. code-block:: bash

   python -m limecore_example eco

To run the CLI tool:

.. code-block:: bash

   python -m limecore_example cli --help
