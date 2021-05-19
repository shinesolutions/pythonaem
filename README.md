[![Build Status](https://github.com/shinesolutions/pythonaem/workflows/CI/badge.svg)](https://github.com/shinesolutions/pythonaem/actions?query=workflow%3ACI)
[![Published Version](https://badge.fury.io/py/pythonaem.svg)](https://pypi.org/project/pythonaem/)
[![Vulnerability Scanning Status](https://snyk.io/test/github/shinesolutions/pythonaem/badge.svg)](https://snyk.io/test/github/shinesolutions/pythonaem)

PythonAEM
---------

PythonAEM is a Python client for [Adobe Experience Manager (AEM)](http://www.adobe.com/au/marketing-cloud/enterprise-content-management.html) API.
It is written on top of [pyswaggeraem](https://github.com/shinesolutions/swagger-aem/blob/master/python/README.md) and provides resource-oriented API and convenient response handling.

Learn more about PythonAEM:

* [Installation](https://github.com/shinesolutions/pythonaem#installation)
* [Usage](https://github.com/shinesolutions/pythonaem#usage)
* [Result Model](https://github.com/shinesolutions/pythonaem#result)
* [Error Handling](https://github.com/shinesolutions/pythonaem#error-handling)
* [Testing](https://github.com/shinesolutions/pythonaem#testing)
* [Versions History](https://github.com/shinesolutions/pythonaem/blob/master/docs/versions.md)

pythonaem is part of [AEM OpenCloud](https://aemopencloud.io) platform but it can be used as a stand-alone.

Installation
------------

    pip3 install pythonaem

Usage
-----

Initialise client:

    from pythonaem import PythonAem

    conf = {
        'username': 'admin',
        'password': 'admin',
        'protocol': 'http',
        'host': 'localhost',
        'port': 4502,
    }
    aem = PythonAem(conf)

Aem:

    result = aem.get_aem_health_check({
        'tags': 'shallow',
        'combine_tags_or': 'false',
    })

Flush agent:

    flush_agent = aem.flush_agent('author', 'some-flush-agent')

    # create or update flush agent
    result = flush_agent.create_update('Some Flush Agent Title', 'Some flush agent description', 'http://somehost:8080')

    # check flush agent's existence
    result = flush_agent.exists()

    # delete flush agent
    result = flush_agent.delete()

Replication agent:

    replication_agent = aem.replication_agent('author', 'some-flush-agent')

    # create or update replication agent
    result = replication_agent('author', 'some-replication-agent')

    # check replication agent's existence
    result = replication_agent.exists()

    # delete replication agent
    result = replication_agent.delete()

Result
------

Each of the above method calls returns a [Result](https://github.com/shinesolutions/pythonaem/blob/master/pythonaem/result.py), which contains message, [Response](https://github.com/shinesolutions/pythonaem/blob/master/pythonaem/response.py), and data payload. For example:


    flush_agent = aem.flush_agent('author', 'some-inexisting-flush-agent')
    result = flush_agent.delete()
    print(result.message)
    print(result.response.status_code)
    print(result.response.body)
    print(result.response.headers)
    print(result.data)

Error Handling
--------------

    flush_agent = aem.flush_agent('author', 'some-inexisting-flush-agent')
    try:
        result = flush_agent.delete()
    except Exception as error:
        self.assertEqual(error.message, 'Flush agent some-inexisting-flush-agent not found on author')

Testing
-------

Integration tests require an AEM instance with [Shine Solutions AEM Health Check](https://github.com/shinesolutions/aem-healthcheck) package installed.

By default it uses AEM running on http://localhost:4502 with `admin` username and `admin` password. AEM instance parameters can be configured using environment variables `aem_protocol`, `aem_host`, `aem_port`, `aem_username`, and `aem_password`.
