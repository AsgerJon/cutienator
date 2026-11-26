//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgcsshandler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtSvg/qtsvgglobal.h>
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#if QT_CONFIG(cssparser)
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgcsshandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(cssparser)
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcssparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#if QT_CONFIG(cssparser)
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgcssvalues_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif

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

//  QSvgCssEasingPtr
//      QSvgCssHandler::createEasing(QSvgCssValues::EasingFunction
//      easingFunction, const QSvgCssValues::EasingValues &values)
extern "C" Q_DECL_EXPORT
QSvgCssEasingPtr *ritual_ZN14QSvgCssHandler12createEasingEN13QSvgCssValues14EasingFunctionERKSt7variantIJNS0_19BezierControlPointsENS0_10StepValuesEEE(
    QSvgCssValues::EasingFunction easingFunction,
    const QSvgCssValues::EasingValues *values) {
  return new QSvgCssEasingPtr(
      QSvgCssHandler::createEasing(
          easingFunction,
          *values));
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

//  void QSvgCssHandler::parseCSStoXMLAttrs(const QList<QCss::Declaration>
//      &declarations, QXmlStreamAttributes &attributes) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QSvgCssHandler18parseCSStoXMLAttrsERK5QListIN4QCss11DeclarationEER20QXmlStreamAttributes(
    const QSvgCssHandler *self,
    const QList<QCss::Declaration> *declarations,
    QXmlStreamAttributes *attributes) {
  self->parseCSStoXMLAttrs(*declarations, *attributes);
}

//  void QSvgCssHandler::parseCSStoXMLAttrs(const QString &css,
//      QXmlStreamAttributes &attributes) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QSvgCssHandler18parseCSStoXMLAttrsERK7QStringR20QXmlStreamAttributes(
    const QSvgCssHandler *self,
    const QString *css,
    QXmlStreamAttributes *attributes) {
  self->parseCSStoXMLAttrs(*css, *attributes);
}

//  void QSvgCssHandler::styleLookup(QSvgNode *node, QXmlStreamAttributes
//      &attributes) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QSvgCssHandler11styleLookupEP8QSvgNodeR20QXmlStreamAttributes(
    const QSvgCssHandler *self,
    QSvgNode *node,
    QXmlStreamAttributes *attributes) {
  self->styleLookup(node, *attributes);
}

//  QSvgCssEasingPtr
//      QSvgCssHandler::createEasingFromKeyword(QSvgCssValues::EasingFunction
//      easingFunction)
extern "C" Q_DECL_EXPORT
QSvgCssEasingPtr *ritual_ZN14QSvgCssHandler23createEasingFromKeywordEN13QSvgCssValues14EasingFunctionE(
    QSvgCssValues::EasingFunction easingFunction) {
  return new QSvgCssEasingPtr(
      QSvgCssHandler::createEasingFromKeyword(
          easingFunction));
}

//  QSvgCssEasingPtr QSvgCssHandler::createStepsEasing(const
//      QSvgCssValues::StepValues &values)
extern "C" Q_DECL_EXPORT
QSvgCssEasingPtr *ritual_ZN14QSvgCssHandler17createStepsEasingERKN13QSvgCssValues10StepValuesE(
    const QSvgCssValues::StepValues *values) {
  return new QSvgCssEasingPtr(QSvgCssHandler::createStepsEasing(*values));
}

//  a QSvgCssEasingPtr a ritual of QSvgCssHandler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSvgCssHandler__QSvgCssEasingPtr(QSvgCssEasingPtr *self) {
  delete self;
}

#endif  // QT_CONFIG(cssparser)
