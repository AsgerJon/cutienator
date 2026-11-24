//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgcsshandler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgcsshandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcssparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSvgCssHandler::QSvgCssHandler()
extern "C" Q_DECL_EXPORT
QSvgCssHandler *ritual_ZN14QSvgCssHandlerC1Ev() {
  return new QSvgCssHandler();
}

//  QSvgCssHandler::~QSvgCssHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSvgCssHandlerD1Ev(QSvgCssHandler *self) {
  delete self;
}

//  QSvgCssAnimation *QSvgCssHandler::createAnimation(QStringView name)
extern "C" Q_DECL_EXPORT
QSvgCssAnimation *ritual_ZN14QSvgCssHandler15createAnimationE11QStringView(
    QSvgCssHandler *self,
    const QString *name) {
  return self->createAnimation(QStringView(*name));
}

//  void QSvgCssHandler::collectAnimations(const QCss::StyleSheet &sheet)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSvgCssHandler17collectAnimationsERKN4QCss10StyleSheetE(
    QSvgCssHandler *self,
    const QCss::StyleSheet *sheet) {
  self->collectAnimations(*sheet);
}

//  void QSvgCssHandler::parseStyleSheet(const QStringView str)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSvgCssHandler15parseStyleSheetE11QStringView(
    QSvgCssHandler *self,
    const QString *str) {
  self->parseStyleSheet(QStringView(*str));
}

//  QString QSvgCssHandler::parseDecltoString(const QCss::Declaration &decl)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QSvgCssHandler17parseDecltoStringERKN4QCss11DeclarationE(
    const QCss::Declaration *decl) {
  return new QString(QSvgCssHandler::parseDecltoString(*decl));
}
