## 0.9.2 (2020-07-31)

ENHANCEMENTS:

- Improve testing with `requests_mock`
- Add `InvalidResponseException` and `HTTPStatusException`
- Add `request_uuid` to response and exception logging
- Add default exception middileware
- Change documentation url
- Update all APIs of `UCloudStack`

BUG FIXES:

- Fix `pytest` version compatible

## 0.9.1 (2020-06-05)

ENHANCEMENTS:

- Add `CreateCertificate` api
- Add `DescribeCertificate` api
- Add `DeleteCertificate` api
- Add `DescribeOPLogs` api
- Update `DescribeVMInstance` api
- Update `CreateVS` api

## 0.9.0 (2020-05-21)

FEATURES:

- Add `ucloudstack` product

ENHANCEMENTS:

- Add `deprecated` decorator

## 0.8.2 (2020-03-12)

BUG FIXES:

- Fix `DescribeSubnetResource`

## 0.8.1 (2020-03-11)

ENHANCEMENTS:

- Update `DescribeSubnet` api

## 0.8.0 (2019-12-03)

FEATURES:

- Add `ufs` product (#42)

## 0.7.0 (2019-11-21)

FEATURES:

- Add ssl options of client (#37)

ENHANCEMENTS:

- Add testing report use ucloud test framework (#38)

## 0.6.2 (2019-10-25)

ENHANCEMENTS:

- Update fields of `UHost` api
- Add `DescribeIsolationGroup ` of `UHost`
- Add `DescribeUHostInstanceSnapshot` of `UHost`

BUG FIXES:

- Fix fields of `BatchDescribeNewUcdnDomain`

## 0.6.1 (2019-10-25)

BUG FIXES:

- fix `UCDN` response fields

## 0.6.0 (2019-10-23)

FEATURES:

- add `UCDN` product

ENHANCEMENTS:

- Add toolkit for auto release

