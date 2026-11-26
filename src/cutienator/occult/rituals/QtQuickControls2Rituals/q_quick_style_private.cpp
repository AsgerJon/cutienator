//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickControls2/6.12.0/QtQuickControls2/private/qquickstyle_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2/QtQuickControls2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2/6.12.0/QtQuickControls2/private/qquickstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/QSharedPointer>
#include <QtCore/QSettings>
#include <QtCore/QString>

//  QString QQuickStylePrivate::style()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickStylePrivate5styleEv() {
  return new QString(QQuickStylePrivate::style());
}

//  QString QQuickStylePrivate::effectiveStyleName(const QString &styleName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickStylePrivate18effectiveStyleNameERK7QString(
    const QString *styleName) {
  return new QString(QQuickStylePrivate::effectiveStyleName(*styleName));
}

//  QString QQuickStylePrivate::fallbackStyle()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickStylePrivate13fallbackStyleEv() {
  return new QString(QQuickStylePrivate::fallbackStyle());
}

//  bool QQuickStylePrivate::isCustomStyle()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickStylePrivate13isCustomStyleEv() {
  return QQuickStylePrivate::isCustomStyle();
}

//  bool QQuickStylePrivate::isResolved()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickStylePrivate10isResolvedEv() {
  return QQuickStylePrivate::isResolved();
}

//  bool QQuickStylePrivate::isUsingDefaultStyle()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickStylePrivate19isUsingDefaultStyleEv() {
  return QQuickStylePrivate::isUsingDefaultStyle();
}

//  void QQuickStylePrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStylePrivate4initEv() {
  QQuickStylePrivate::init();
}

//  void QQuickStylePrivate::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStylePrivate5resetEv() {
  QQuickStylePrivate::reset();
}

//  QString QQuickStylePrivate::configFilePath()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickStylePrivate14configFilePathEv() {
  return new QString(QQuickStylePrivate::configFilePath());
}

//  QSharedPointer<QSettings> QQuickStylePrivate::settings(const QString
//      &group)
extern "C" Q_DECL_EXPORT
QSharedPointer<QSettings> *ritual_ZN18QQuickStylePrivate8settingsERK7QString(
    const QString *group) {
  return new QSharedPointer<QSettings>(QQuickStylePrivate::settings(*group));
}

//  const QFont *QQuickStylePrivate::readFont(const QSharedPointer<QSettings>
//      &settings)
extern "C" Q_DECL_EXPORT
const QFont *ritual_ZN18QQuickStylePrivate8readFontERK14QSharedPointerI9QSettingsE(
    const QSharedPointer<QSettings> *settings) {
  return QQuickStylePrivate::readFont(*settings);
}

//  const QPalette *QQuickStylePrivate::readPalette(const
//      QSharedPointer<QSettings> &settings)
extern "C" Q_DECL_EXPORT
const QPalette *ritual_ZN18QQuickStylePrivate11readPaletteERK14QSharedPointerI9QSettingsE(
    const QSharedPointer<QSettings> *settings) {
  return QQuickStylePrivate::readPalette(*settings);
}

//  bool QQuickStylePrivate::isDarkSystemTheme()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickStylePrivate17isDarkSystemThemeEv() {
  return QQuickStylePrivate::isDarkSystemTheme();
}

//  QStringList QQuickStylePrivate::builtInStyles()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN18QQuickStylePrivate13builtInStylesEv() {
  return new QList<QString>(QQuickStylePrivate::builtInStyles());
}

//  QQuickStylePrivate::~QQuickStylePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStylePrivateD1Ev(QQuickStylePrivate *self) {
  delete self;
}

//  a QSharedPointer<QSettings> a ritual of QQuickStylePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickStylePrivate__QSharedPointer_QSettings(
    QSharedPointer<QSettings> *self) {
  delete self;
}
