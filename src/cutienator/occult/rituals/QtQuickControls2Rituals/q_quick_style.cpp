//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickControls2/qquickstyle.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickControls2/QtQuickControls2>
#include <QtQuickControls2/qquickstyle.h>
#include <QtCore/qstring.h>

//  QString QQuickStyle::name()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickStyle4nameEv() {
  return new QString(QQuickStyle::name());
}

//  void QQuickStyle::setStyle(const QString &style)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickStyle8setStyleERK7QString(const QString *style) {
  QQuickStyle::setStyle(*style);
}

//  void QQuickStyle::setFallbackStyle(const QString &style)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickStyle16setFallbackStyleERK7QString(
    const QString *style) {
  QQuickStyle::setFallbackStyle(*style);
}

//  QQuickStyle::~QQuickStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickStyleD1Ev(QQuickStyle *self) {
  delete self;
}
