//  Edited by hand on 2026-11-25: the include of
//  QtCore/private/qxmlstreamparser_p.h is taken out, as it defines
//  inline functions using 'getChar', 'reallocateStack' and others that
//  Qt defines only in qxmlstream.cpp, which the compiler warned of
//  and the test build refused; no ritual here needs it. Kept as it is
//  when the generator runs again.
//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qxmlstream_p.h, Qt 6.12.0.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(xmlstream)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qxmlstream_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "QtCore/qxmlstream.h"
#if QT_CONFIG(xmlstream)
#include <QtCore/private/qxmlutils_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <stdio.h>
#include <QtCore/qstringconverter.h>
#include <QtCore/qstack.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <QtCore/private/qtools_p.h>
#include <iterator>
#include <QtCore/private/qxmlstream_p.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/private/qstringiterator_p.h>
#include <algorithm>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/serialization/qxmlstream.cpp, line 1008, as _ZN25QXmlStreamPrivateTagStackC1Ev
#if QT_CONFIG(xmlstream)
inline QXmlStreamPrivateTagStack::QXmlStreamPrivateTagStack()
{
    tagStack.reserve(16);
    tagStackStringStorageSize = 0;
    NamespaceDeclaration &namespaceDeclaration = namespaceDeclarations.push();
    namespaceDeclaration.namespaceUri = addToStringStorage(u"http://www.w3.org/XML/1998/namespace");
    namespaceDeclaration.prefix = addToStringStorage(u"xml");
    initialTagStackStringStorageSize = tagStackStringStorageSize;
    tagsDone = false;
}
#endif  // QT_CONFIG(xmlstream)
//  -----------------------------------------------------------------------

//  QXmlStreamPrivateTagStack::QXmlStreamPrivateTagStack()
extern "C" Q_DECL_EXPORT
QXmlStreamPrivateTagStack *ritual_ZN25QXmlStreamPrivateTagStackC1Ev() {
  return new QXmlStreamPrivateTagStack();
}

//  XmlStringRef QXmlStreamPrivateTagStack::addToStringStorage(QAnyStringView
//      s)
extern "C" Q_DECL_EXPORT
QtPrivate::XmlStringRef *ritual_ZN25QXmlStreamPrivateTagStack18addToStringStorageE14QAnyStringView(
    QXmlStreamPrivateTagStack *self,
    const QString *s) {
  return new QtPrivate::XmlStringRef(
      self->addToStringStorage(
          QAnyStringView(*s)));
}

//  Tag QXmlStreamPrivateTagStack::tagStack_pop()
extern "C" Q_DECL_EXPORT
QXmlStreamPrivateTagStack::Tag *ritual_ZN25QXmlStreamPrivateTagStack12tagStack_popEv(
    QXmlStreamPrivateTagStack *self) {
  return new QXmlStreamPrivateTagStack::Tag(self->tagStack_pop());
}

//  Tag &QXmlStreamPrivateTagStack::tagStack_push()
extern "C" Q_DECL_EXPORT
QXmlStreamPrivateTagStack::Tag *ritual_ZN25QXmlStreamPrivateTagStack13tagStack_pushEv(
    QXmlStreamPrivateTagStack *self) {
  return &(self->tagStack_push());
}

#endif  // QT_CONFIG(xmlstream)
