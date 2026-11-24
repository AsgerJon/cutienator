//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qxmlstream_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstreamreader)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qxmlstream_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>

//  QXmlStreamReaderPrivate::Entity::Entity()
extern "C" Q_DECL_EXPORT
QXmlStreamReaderPrivate::Entity *ritual_ZN23QXmlStreamReaderPrivate6EntityC1Ev() {
  return new QXmlStreamReaderPrivate::Entity();
}

//  QXmlStreamReaderPrivate::Entity::Entity(const QString &name, const
//      QString &value)
extern "C" Q_DECL_EXPORT
QXmlStreamReaderPrivate::Entity *ritual_ZN23QXmlStreamReaderPrivate6EntityC1ERK7QStringS3_(
    const QString *name,
    const QString *value) {
  return new QXmlStreamReaderPrivate::Entity(*name, *value);
}

//  Entity QXmlStreamReaderPrivate::Entity::createLiteral(QLatin1StringView
//      name, QLatin1StringView value)
extern "C" Q_DECL_EXPORT
QXmlStreamReaderPrivate::Entity *ritual_ZN23QXmlStreamReaderPrivate6Entity13createLiteralE13QLatin1StringS1_(
    const QLatin1String *name,
    const QLatin1String *value) {
  return new QXmlStreamReaderPrivate::Entity(
      QXmlStreamReaderPrivate::Entity::createLiteral(
          *name,
          *value));
}

//  QXmlStreamReaderPrivate::Entity::~Entity()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlStreamReaderPrivate6EntityD1Ev(
    QXmlStreamReaderPrivate::Entity *self) {
  delete self;
}

#endif  // QT_CONFIG(xmlstreamreader)
#endif  // QT_CONFIG(xmlstream)
