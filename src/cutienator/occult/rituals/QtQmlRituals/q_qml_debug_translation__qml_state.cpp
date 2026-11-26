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

//  QQmlDebugTranslation::QmlState::QmlState()
extern "C" Q_DECL_EXPORT
QQmlDebugTranslation::QmlState *ritual_ZN20QQmlDebugTranslation8QmlStateC1Ev() {
  return new QQmlDebugTranslation::QmlState();
}

//  QDataStream &operator>>(QDataStream &stream, QmlState &qmlState)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN20QQmlDebugTranslationrsER11QDataStreamRNS_8QmlStateE(
    QDataStream *stream,
    QQmlDebugTranslation::QmlState *qmlState) {
  return &(operator>>(*stream, *qmlState));
}

//  QDataStream &operator<<(QDataStream &stream, const QmlState &qmlState)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZN20QQmlDebugTranslationlsER11QDataStreamRKNS_8QmlStateE(
    QDataStream *stream,
    const QQmlDebugTranslation::QmlState *qmlState) {
  return &(operator<<(*stream, *qmlState));
}

//  QQmlDebugTranslation::QmlState::~QmlState()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDebugTranslation8QmlStateD1Ev(
    QQmlDebugTranslation::QmlState *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_debug)
