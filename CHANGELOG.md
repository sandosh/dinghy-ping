# Dinghy-ping CHANGELOG

This file is used to list changes made in each version of the Dinghy-ping 

## unreleased

## v0.1.0 (2019-05-22)

- [Zane Williamson] - Upgrade to Tailwind CSS v1.0 and lock in version

## v0.0.17 (2019-05-01)

- [Zane Williamson] - Moving history to upper right, adding slivermullet logo 

## v0.0.16 (2019-05-01)

- [Zane Williamson] - Security and dependency updates 

## v0.0.15 (2019-01-26)

- [Zane Williamson] - Save tcp tests to history, Travis test with Python 3.7 

## v0.0.14 (2019-01-14)

- [Zane Williamson] - Adding TCP check feature

## v0.0.13 (2019-01-13)

- [Zane Williamson] - Fix https://github.com/silvermullet/dinghy-ping/issues/39, better error handling, deliever results even if redis not available 

## v0.0.12 (2019-01-10)

- [Zane Williamson] - Adding header input support, using Tailwind CSS for form

## v0.0.11 (2018-12-29)

- [Zane Williamson]
  * Exposing Prometheus metrics
  * Fix starlette dependency version issue (see here)[https://github.com/kennethreitz/responder/issues/266]
  * Updating local development docs

## v0.0.10 (2018-11-22)

- [Zane Williamson] - Adding response code and response time to history

## v0.0.9 (2018-11-22)

- [Zane Williamson] - Add redis support for storing and retrieving ping results, present history on input page
- [Ian Morgan] - Adding redis side car with pvc to Helm chart 

## v0.0.8 (2018-11-19)

- [Zane Williamson] - Add link back to search form 
- [Ian Morgan] - Fix timeout issue in Issue [28](https://github.com/silvermullet/dinghy-ping/issues/28)

## v0.0.7 (2018-11-13)

- [Zane Williamson] - Spruce up ping response template, using Tailwind CSS

## v0.0.6 (2018-11-13)

- [Zane Williamson]
 * Include full request in ping results page
 * Set default scheme to https if none requested - fix issue [25](https://github.com/silvermullet/dinghy-ping/issues/25)

## v0.0.5 (2018-11-01)

- [Ian Morgan] - Form input on landing page. HAWT 

## v0.0.4 (2018-10-29)

- [Zane Williamson] - Better error handling on request process 

## v0.0.3 (2018-10-28)

- [Zane Williamson] - Refactor multiple domain response, adding intial pytests 

## v0.0.2 (2018-10-22)

- [Zane Williamson] - Adding multiple domain support, travis build process for docker 
