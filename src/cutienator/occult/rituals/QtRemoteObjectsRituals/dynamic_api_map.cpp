//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qmetaobjectbuilder_p.h>
#include <QtRemoteObjects/private/qremoteobjectcontainers_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/private/qremoteobjectnode_p.h>
#include <QtRemoteObjects/qremoteobjectregistry.h>
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/private/qremoteobjectregistrysource_p.h>
#include <QtRemoteObjects/private/qremoteobjectreplica_p.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#include <QtCore/qabstractitemmodel.h>
#include <memory>
#include <algorithm>
#include <QtRemoteObjects/qremoteobjectsource.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <QtRemoteObjects/private/qremoteobjectsourceio_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qabstractitemmodel.h>
#include <algorithm>
#include <iterator>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace QRemoteObjectStringLiterals;

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 247, as _ZN15QtRemoteObjects37getTypeNameAndMetaobjectFromClassInfoERPK11QMetaObject
inline QString QtRemoteObjects::getTypeNameAndMetaobjectFromClassInfo(const QMetaObject *& meta) {
    QString typeName;
    const int ind = meta->indexOfClassInfo(QCLASSINFO_REMOTEOBJECT_TYPE);
    if (ind != -1) { //We have an object created from repc or at least with QCLASSINFO defined
        typeName = QString::fromLatin1(meta->classInfo(ind).value());
        while (true) {
            Q_ASSERT(meta->superClass());//This recurses to QObject, which doesn't have QCLASSINFO_REMOTEOBJECT_TYPE
            //At the point superclass doesn't have the same QCLASSINFO_REMOTEOBJECT_TYPE,
            //we have the metaobject we should work from
            if (ind != meta->superClass()->indexOfClassInfo(QCLASSINFO_REMOTEOBJECT_TYPE))
                break;
            meta = meta->superClass();
        }
    }
    return typeName;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 609, as _ZNK13DynamicApiMap20signalParameterNamesEi
inline QByteArrayList DynamicApiMap::signalParameterNames(int index) const
{
    const int objectIndex = m_signals.at(index);
    checkCache(objectIndex);
    return m_cachedMetamethod.parameterNames();
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 634, as _ZNK13DynamicApiMap10methodTypeEi
inline QMetaMethod::MethodType DynamicApiMap::methodType(int index) const
{
    const int objectIndex = m_methods.at(index);
    checkCache(objectIndex);
    return m_cachedMetamethod.methodType();
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 641, as _ZNK13DynamicApiMap8typeNameEi
inline const QByteArray DynamicApiMap::typeName(int index) const
{
    const int objectIndex = m_methods.at(index);
    checkCache(objectIndex);
    return m_cachedMetamethod.typeName();
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 648, as _ZNK13DynamicApiMap20methodParameterNamesEi
inline QByteArrayList DynamicApiMap::methodParameterNames(int index) const
{
    const int objectIndex = m_methods.at(index);
    checkCache(objectIndex);
    return m_cachedMetamethod.parameterNames();
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 616, as _ZNK13DynamicApiMap14parameterCountEi
inline int DynamicApiMap::parameterCount(int objectIndex) const
{
    checkCache(objectIndex);
    return m_cachedMetamethod.parameterCount();
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 622, as _ZNK13DynamicApiMap13parameterTypeEii
inline int DynamicApiMap::parameterType(int objectIndex, int paramIndex) const
{
    checkCache(objectIndex);
    return m_cachedMetamethod.parameterType(paramIndex);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 628, as _ZNK13DynamicApiMap9signatureEi
inline const QByteArray DynamicApiMap::signature(int objectIndex) const
{
    checkCache(objectIndex);
    return m_cachedMetamethod.methodSignature();
}
//  -----------------------------------------------------------------------

//  DynamicApiMap::~DynamicApiMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DynamicApiMapD1Ev(DynamicApiMap *self) {
  delete self;
}

//  QString DynamicApiMap::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DynamicApiMap4nameEv(const DynamicApiMap *self) {
  return new QString(self->name());
}

//  QString DynamicApiMap::typeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DynamicApiMap8typeNameEv(const DynamicApiMap *self) {
  return new QString(self->typeName());
}

//  QByteArray DynamicApiMap::className() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13DynamicApiMap9classNameEv(
    const DynamicApiMap *self) {
  return new QByteArray(self->className());
}

//  int DynamicApiMap::enumCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap9enumCountEv(const DynamicApiMap *self) {
  return self->enumCount();
}

//  int DynamicApiMap::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap13propertyCountEv(const DynamicApiMap *self) {
  return self->propertyCount();
}

//  int DynamicApiMap::signalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap11signalCountEv(const DynamicApiMap *self) {
  return self->signalCount();
}

//  int DynamicApiMap::methodCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap11methodCountEv(const DynamicApiMap *self) {
  return self->methodCount();
}

//  int DynamicApiMap::sourceEnumIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap15sourceEnumIndexEi(
    const DynamicApiMap *self,
    int index) {
  return self->sourceEnumIndex(index);
}

//  int DynamicApiMap::sourcePropertyIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap19sourcePropertyIndexEi(
    const DynamicApiMap *self,
    int index) {
  return self->sourcePropertyIndex(index);
}

//  int DynamicApiMap::sourceSignalIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap17sourceSignalIndexEi(
    const DynamicApiMap *self,
    int index) {
  return self->sourceSignalIndex(index);
}

//  int DynamicApiMap::sourceMethodIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap17sourceMethodIndexEi(
    const DynamicApiMap *self,
    int index) {
  return self->sourceMethodIndex(index);
}

//  int DynamicApiMap::signalParameterCount(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap20signalParameterCountEi(
    const DynamicApiMap *self,
    int index) {
  return self->signalParameterCount(index);
}

//  int DynamicApiMap::signalParameterType(int sigIndex, int paramIndex)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap19signalParameterTypeEii(
    const DynamicApiMap *self,
    int sigIndex,
    int paramIndex) {
  return self->signalParameterType(sigIndex, paramIndex);
}

//  const QByteArray DynamicApiMap::signalSignature(int index) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13DynamicApiMap15signalSignatureEi(
    const DynamicApiMap *self,
    int index) {
  return new QByteArray(self->signalSignature(index));
}

//  QByteArrayList DynamicApiMap::signalParameterNames(int index) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK13DynamicApiMap20signalParameterNamesEi(
    const DynamicApiMap *self,
    int index) {
  return new QList<QByteArray>(self->signalParameterNames(index));
}

//  int DynamicApiMap::methodParameterCount(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap20methodParameterCountEi(
    const DynamicApiMap *self,
    int index) {
  return self->methodParameterCount(index);
}

//  int DynamicApiMap::methodParameterType(int methodIndex, int paramIndex)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap19methodParameterTypeEii(
    const DynamicApiMap *self,
    int methodIndex,
    int paramIndex) {
  return self->methodParameterType(methodIndex, paramIndex);
}

//  const QByteArray DynamicApiMap::methodSignature(int index) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13DynamicApiMap15methodSignatureEi(
    const DynamicApiMap *self,
    int index) {
  return new QByteArray(self->methodSignature(index));
}

//  QMetaMethod::MethodType DynamicApiMap::methodType(int index) const
extern "C" Q_DECL_EXPORT
QMetaMethod::MethodType ritual_ZNK13DynamicApiMap10methodTypeEi(
    const DynamicApiMap *self,
    int index) {
  return self->methodType(index);
}

//  const QByteArray DynamicApiMap::typeName(int index) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13DynamicApiMap8typeNameEi(
    const DynamicApiMap *self,
    int index) {
  return new QByteArray(self->typeName(index));
}

//  QByteArrayList DynamicApiMap::methodParameterNames(int index) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK13DynamicApiMap20methodParameterNamesEi(
    const DynamicApiMap *self,
    int index) {
  return new QList<QByteArray>(self->methodParameterNames(index));
}

//  int DynamicApiMap::propertyIndexFromSignal(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap23propertyIndexFromSignalEi(
    const DynamicApiMap *self,
    int index) {
  return self->propertyIndexFromSignal(index);
}

//  int DynamicApiMap::propertyRawIndexFromSignal(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap26propertyRawIndexFromSignalEi(
    const DynamicApiMap *self,
    int index) {
  return self->propertyRawIndexFromSignal(index);
}

//  QByteArray DynamicApiMap::objectSignature() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13DynamicApiMap15objectSignatureEv(
    const DynamicApiMap *self) {
  return new QByteArray(self->objectSignature());
}

//  bool DynamicApiMap::isDynamic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DynamicApiMap9isDynamicEv(const DynamicApiMap *self) {
  return self->isDynamic();
}

//  int DynamicApiMap::parameterCount(int objectIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap14parameterCountEi(
    const DynamicApiMap *self,
    int objectIndex) {
  return self->parameterCount(objectIndex);
}

//  int DynamicApiMap::parameterType(int objectIndex, int paramIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13DynamicApiMap13parameterTypeEii(
    const DynamicApiMap *self,
    int objectIndex,
    int paramIndex) {
  return self->parameterType(objectIndex, paramIndex);
}

//  const QByteArray DynamicApiMap::signature(int objectIndex) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13DynamicApiMap9signatureEi(
    const DynamicApiMap *self,
    int objectIndex) {
  return new QByteArray(self->signature(objectIndex));
}

//  void DynamicApiMap::checkCache(int objectIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13DynamicApiMap10checkCacheEi(
    const DynamicApiMap *self,
    int objectIndex) {
  self->checkCache(objectIndex);
}
