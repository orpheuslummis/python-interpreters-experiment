# python313-interpreters-experiment

This repository contains a hypothetical experiment to measure the memory overhead of using multiple interpreters in Python, based on the proposed PEP 734.

PEP 734 proposes adding a new interpreters module to Python’s standard library, allowing for the creation and management of multiple interpreters within a single Python process. This experiment evaluates the memory overhead associated with this feature.

Note: This experiment is hypothetical and based on the proposed PEP 734. The interpreters module and its functionality are not yet available in Python. This code is a conceptual demonstration of how the experiment could be conducted if PEP 734 is accepted and implemented in a future Python release (potentially Python 3.14).

The experiment involves:

	1.	Measuring the baseline memory usage of a Python process without additional interpreters.
	2.	Creating multiple interpreters and measuring the memory usage to determine the overhead.
	3.	Optionally loading a standard library module in each interpreter to measure additional memory overhead.

The experiment runs multiple times to compute average memory usage and standard deviation, providing a detailed analysis of the memory overhead.