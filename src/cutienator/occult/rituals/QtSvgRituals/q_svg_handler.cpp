//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvghandler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvghandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qstringview.h>
#include <QtGui/qpen.h>
#include <QtCore/qxmlstream.h>

//  QSvgHandler::QSvgHandler(QIODevice *device, QtSvg::Options options,
//      QtSvg::AnimatorType type)
extern "C" Q_DECL_EXPORT
QSvgHandler *ritual_ZN11QSvgHandlerC1EP9QIODevice6QFlagsIN5QtSvg6OptionEENS3_12AnimatorTypeE(
    QIODevice *device,
    int options,
    QtSvg::AnimatorType type) {
  return new QSvgHandler(
      device,
      QFlags<QtSvg::Option>::fromInt(options),
      type);
}

//  QSvgHandler::QSvgHandler(const QByteArray &data, QtSvg::Options options,
//      QtSvg::AnimatorType type)
extern "C" Q_DECL_EXPORT
QSvgHandler *ritual_ZN11QSvgHandlerC1ERK10QByteArray6QFlagsIN5QtSvg6OptionEENS4_12AnimatorTypeE(
    const QByteArray *data,
    int options,
    QtSvg::AnimatorType type) {
  return new QSvgHandler(
      *data,
      QFlags<QtSvg::Option>::fromInt(options),
      type);
}

//  QSvgHandler::~QSvgHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandlerD1Ev(QSvgHandler *self) {
  delete self;
}

//  QIODevice *QSvgHandler::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK11QSvgHandler6deviceEv(const QSvgHandler *self) {
  return self->device();
}

//  QSvgDocument *QSvgHandler::document() const
extern "C" Q_DECL_EXPORT
QSvgDocument *ritual_ZNK11QSvgHandler8documentEv(const QSvgHandler *self) {
  return self->document();
}

//  bool QSvgHandler::ok() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSvgHandler2okEv(const QSvgHandler *self) {
  return self->ok();
}

//  QString QSvgHandler::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QSvgHandler11errorStringEv(const QSvgHandler *self) {
  return new QString(self->errorString());
}

//  int QSvgHandler::lineNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSvgHandler10lineNumberEv(const QSvgHandler *self) {
  return self->lineNumber();
}

//  void QSvgHandler::setDefaultCoordinateSystem(QGuiSvg::LengthType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler26setDefaultCoordinateSystemEN7QGuiSvg10LengthTypeE(
    QSvgHandler *self,
    QGuiSvg::LengthType type) {
  self->setDefaultCoordinateSystem(type);
}

//  QGuiSvg::LengthType QSvgHandler::defaultCoordinateSystem() const
extern "C" Q_DECL_EXPORT
QGuiSvg::LengthType ritual_ZNK11QSvgHandler23defaultCoordinateSystemEv(
    const QSvgHandler *self) {
  return self->defaultCoordinateSystem();
}

//  void QSvgHandler::pushColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler9pushColorERK6QColor(
    QSvgHandler *self,
    const QColor *color) {
  self->pushColor(*color);
}

//  void QSvgHandler::pushColorCopy()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler13pushColorCopyEv(QSvgHandler *self) {
  self->pushColorCopy();
}

//  void QSvgHandler::popColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler8popColorEv(QSvgHandler *self) {
  self->popColor();
}

//  QColor QSvgHandler::currentColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QSvgHandler12currentColorEv(const QSvgHandler *self) {
  return new QColor(self->currentColor());
}

//  void QSvgHandler::pushUnresolvedStyle(QSvgStyleProperty *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler19pushUnresolvedStyleEP17QSvgStyleProperty(
    QSvgHandler *self,
    QSvgStyleProperty *prop) {
  self->pushUnresolvedStyle(prop);
}

//  void QSvgHandler::setCurrentSvgFontFamily(QStringView family)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler23setCurrentSvgFontFamilyE11QStringView(
    QSvgHandler *self,
    const QString *family) {
  self->setCurrentSvgFontFamily(QStringView(*family));
}

#if !defined(QT_NO_CSSPARSER)
//  void QSvgHandler::setInStyle(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler10setInStyleEb(QSvgHandler *self, bool b) {
  self->setInStyle(b);
}
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
//  bool QSvgHandler::inStyle() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSvgHandler7inStyleEv(const QSvgHandler *self) {
  return self->inStyle();
}
#endif  // !defined(QT_NO_CSSPARSER)

//  void QSvgHandler::setAnimPeriod(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler13setAnimPeriodEii(
    QSvgHandler *self,
    int start,
    int end) {
  self->setAnimPeriod(start, end);
}

//  int QSvgHandler::animationDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSvgHandler17animationDurationEv(const QSvgHandler *self) {
  return self->animationDuration();
}

//  QPen QSvgHandler::defaultPen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK11QSvgHandler10defaultPenEv(const QSvgHandler *self) {
  return new QPen(self->defaultPen());
}

//  QtSvg::Options QSvgHandler::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSvgHandler7optionsEv(const QSvgHandler *self) {
  return static_cast<int>(self->options().toInt());
}

//  QtSvg::AnimatorType QSvgHandler::animatorType() const
extern "C" Q_DECL_EXPORT
QtSvg::AnimatorType ritual_ZNK11QSvgHandler12animatorTypeEv(
    const QSvgHandler *self) {
  return self->animatorType();
}

//  bool QSvgHandler::trustedSourceMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSvgHandler17trustedSourceModeEv(const QSvgHandler *self) {
  return self->trustedSourceMode();
}

//  bool QSvgHandler::startElement(const QStringView localName, const
//      QXmlStreamAttributes &attributes)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgHandler12startElementE11QStringViewRK20QXmlStreamAttributes(
    QSvgHandler *self,
    const QString *localName,
    const QXmlStreamAttributes *attributes) {
  return self->startElement(QStringView(*localName), *attributes);
}

//  bool QSvgHandler::endElement(const QStringView localName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgHandler10endElementE11QStringView(
    QSvgHandler *self,
    const QString *localName) {
  return self->endElement(QStringView(*localName));
}

//  bool QSvgHandler::characters(const QStringView str)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgHandler10charactersE11QStringView(
    QSvgHandler *self,
    const QString *str) {
  return self->characters(QStringView(*str));
}

//  bool QSvgHandler::processingInstruction(const QStringView target, const
//      QStringView data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgHandler21processingInstructionE11QStringViewS0_(
    QSvgHandler *self,
    const QString *target,
    const QString *data) {
  return self->processingInstruction(
      QStringView(*target),
      QStringView(*data));
}

//  void QSvgHandler::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler4initEv(QSvgHandler *self) {
  self->init();
}

//  void QSvgHandler::parse()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler5parseEv(QSvgHandler *self) {
  self->parse();
}

//  void QSvgHandler::resolvePaintServers()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler19resolvePaintServersEv(QSvgHandler *self) {
  self->resolvePaintServers();
}

//  void QSvgHandler::resolveNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgHandler12resolveNodesEv(QSvgHandler *self) {
  self->resolveNodes();
}
