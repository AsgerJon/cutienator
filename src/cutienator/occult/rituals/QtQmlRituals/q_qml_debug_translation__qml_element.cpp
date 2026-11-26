//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugtranslationprotocol_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_debug)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugtranslationprotocol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlDebugTranslation::QmlElement::QmlElement()
extern "C" Q_DECL_EXPORT
QQmlDebugTranslation::QmlElement *ritual_ZN20QQmlDebugTranslation10QmlElementC1Ev() {
  return new QQmlDebugTranslation::QmlElement();
}

//  QDataStream &operator>>(QDataStream &stream, QmlElement &qmlElement)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN20QQmlDebugTranslationrsER11QDataStreamRNS_10QmlElementE(
    QDataStream *stream,
    QQmlDebugTranslation::QmlElement *qmlElement) {
  return &(operator>>(*stream, *qmlElement));
}

//  QDataStream &operator<<(QDataStream &stream, const QmlElement
//      &qmlElement)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN20QQmlDebugTranslationlsER11QDataStreamRKNS_10QmlElementE(
    QDataStream *stream,
    const QQmlDebugTranslation::QmlElement *qmlElement) {
  return &(operator<<(*stream, *qmlElement));
}

//  QQmlDebugTranslation::QmlElement::~QmlElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDebugTranslation10QmlElementD1Ev(
    QQmlDebugTranslation::QmlElement *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_debug)
