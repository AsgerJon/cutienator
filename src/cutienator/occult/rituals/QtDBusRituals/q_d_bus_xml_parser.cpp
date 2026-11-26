//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusxmlparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusxmlparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QSharedDataPointer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/private/qdbusxmlparser_p.h>
#include <QtDBus/private/qdbusutil_p.h>
#include <QtCore/qmap.h>
#include <QtCore/qvariant.h>
#include <QtCore/qtextstream.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/dbus/qdbusxmlparser.cpp, line 359, as _ZN14QDBusXmlParser20readNextStartElementEv
#if !defined(QT_NO_DBUS)
inline bool QDBusXmlParser::readNextStartElement()
{
    updateCurrentLocation();

    while (m_xml.readNext() != QXmlStreamReader::Invalid) {
        if (m_xml.isEndElement())
            return false;
        else if (m_xml.isStartElement())
            return true;
        updateCurrentLocation();
    }
    return false;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusxmlparser.cpp, line 351, as _ZN14QDBusXmlParser21updateCurrentLocationEv
#if !defined(QT_NO_DBUS)
inline void QDBusXmlParser::updateCurrentLocation()
{
    m_currentLocation =
            QDBusIntrospection::SourceLocation{ m_xml.lineNumber(), m_xml.columnNumber() };
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  QDBusIntrospection::Interfaces QDBusXmlParser::interfaces() const
extern "C" Q_DECL_EXPORT
QDBusIntrospection::Interfaces *ritual_ZNK14QDBusXmlParser10interfacesEv(
    const QDBusXmlParser *self) {
  return new QDBusIntrospection::Interfaces(self->interfaces());
}

//  QSharedDataPointer<QDBusIntrospection::Object> QDBusXmlParser::object()
//      const
extern "C" Q_DECL_EXPORT
QSharedDataPointer<QDBusIntrospection::Object> *ritual_ZNK14QDBusXmlParser6objectEv(
    const QDBusXmlParser *self) {
  return new QSharedDataPointer<QDBusIntrospection::Object>(self->object());
}

#if !defined(QT_NO_DBUS)
//  bool QDBusXmlParser::readNextStartElement()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QDBusXmlParser20readNextStartElementEv(
    QDBusXmlParser *self) {
  return self->readNextStartElement();
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusXmlParser::updateCurrentLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDBusXmlParser21updateCurrentLocationEv(
    QDBusXmlParser *self) {
  self->updateCurrentLocation();
}
#endif  // !defined(QT_NO_DBUS)

//  a QDBusIntrospection::Interfaces a ritual of QDBusXmlParser gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusXmlParser__QDBusIntrospection_Interfaces(
    QDBusIntrospection::Interfaces *self) {
  delete self;
}

//  a QSharedDataPointer<QDBusIntrospection::Object> a ritual of
//      QDBusXmlParser gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusXmlParser__QSharedDataPointer_QDBusIntrospection_Object(
    QSharedDataPointer<QDBusIntrospection::Object> *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
