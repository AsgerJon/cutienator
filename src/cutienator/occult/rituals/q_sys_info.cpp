//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsysinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsysinfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  QString QSysInfo::buildCpuArchitecture()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSysInfo20buildCpuArchitectureEv() {
  return new QString(QSysInfo::buildCpuArchitecture());
}

//  QString QSysInfo::currentCpuArchitecture()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSysInfo22currentCpuArchitectureEv() {
  return new QString(QSysInfo::currentCpuArchitecture());
}

//  QString QSysInfo::buildAbi()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSysInfo8buildAbiEv() {
  return new QString(QSysInfo::buildAbi());
}

//  QString QSysInfo::kernelType()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSysInfo10kernelTypeEv() {
  return new QString(QSysInfo::kernelType());
}

//  QString QSysInfo::kernelVersion()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSysInfo13kernelVersionEv() {
  return new QString(QSysInfo::kernelVersion());
}

//  QString QSysInfo::productType()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSysInfo11productTypeEv() {
  return new QString(QSysInfo::productType());
}

//  QString QSysInfo::productVersion()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSysInfo14productVersionEv() {
  return new QString(QSysInfo::productVersion());
}

//  QString QSysInfo::prettyProductName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSysInfo17prettyProductNameEv() {
  return new QString(QSysInfo::prettyProductName());
}

//  QString QSysInfo::machineHostName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QSysInfo15machineHostNameEv() {
  return new QString(QSysInfo::machineHostName());
}

//  QByteArray QSysInfo::machineUniqueId()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN8QSysInfo15machineUniqueIdEv() {
  return new QByteArray(QSysInfo::machineUniqueId());
}

//  QByteArray QSysInfo::bootUniqueId()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN8QSysInfo12bootUniqueIdEv() {
  return new QByteArray(QSysInfo::bootUniqueId());
}

//  QSysInfo::~QSysInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSysInfoD1Ev(QSysInfo *self) {
  delete self;
}
