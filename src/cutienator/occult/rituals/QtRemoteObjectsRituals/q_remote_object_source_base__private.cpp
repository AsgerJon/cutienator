//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 655, as _ZN23QRemoteObjectSourceBase7PrivateC1EP21QRemoteObjectSourceIoP23QRemoteObjectRootSource
inline QRemoteObjectSourceBase::Private::Private(QRemoteObjectSourceIo *io, QRemoteObjectRootSource *root)
    : m_sourceIo(io), codec(io->m_codec.data()), isDynamic(false), root(root)
{
}
//  -----------------------------------------------------------------------

//  QRemoteObjectSourceBase::Private::Private(QRemoteObjectSourceIo *io,
//      QRemoteObjectRootSource *root)
extern "C" Q_DECL_EXPORT
QRemoteObjectSourceBase::Private *ritual_ZN23QRemoteObjectSourceBase7PrivateC1EP21QRemoteObjectSourceIoP23QRemoteObjectRootSource(
    QRemoteObjectSourceIo *io,
    QRemoteObjectRootSource *root) {
  return new QRemoteObjectSourceBase::Private(io, root);
}

//  QRemoteObjectSourceBase::Private::~Private()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRemoteObjectSourceBase7PrivateD1Ev(
    QRemoteObjectSourceBase::Private *self) {
  delete self;
}
