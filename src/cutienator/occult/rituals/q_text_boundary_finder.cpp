//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtextboundaryfinder.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtextboundaryfinder.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QTextBoundaryFinder::QTextBoundaryFinder()
extern "C" Q_DECL_EXPORT
QTextBoundaryFinder *ritual_ZN19QTextBoundaryFinderC1Ev() {
  return new QTextBoundaryFinder();
}

//  QTextBoundaryFinder::QTextBoundaryFinder(const QTextBoundaryFinder
//      &other)
extern "C" Q_DECL_EXPORT
QTextBoundaryFinder *ritual_ZN19QTextBoundaryFinderC1ERKS_(
    const QTextBoundaryFinder *other) {
  return new QTextBoundaryFinder(*other);
}

//  QTextBoundaryFinder::~QTextBoundaryFinder()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextBoundaryFinderD1Ev(QTextBoundaryFinder *self) {
  delete self;
}

//  QTextBoundaryFinder::QTextBoundaryFinder(BoundaryType type, const QString
//      &string)
extern "C" Q_DECL_EXPORT
QTextBoundaryFinder *ritual_ZN19QTextBoundaryFinderC1ENS_12BoundaryTypeERK7QString(
    QTextBoundaryFinder::BoundaryType type,
    const QString *string) {
  return new QTextBoundaryFinder(type, *string);
}

//  QTextBoundaryFinder::QTextBoundaryFinder(BoundaryType type, const QChar
//      *chars, qsizetype length, unsigned char *buffer, qsizetype
//      bufferSize)
extern "C" Q_DECL_EXPORT
QTextBoundaryFinder *ritual_ZN19QTextBoundaryFinderC1ENS_12BoundaryTypeEPK5QCharxPhx(
    QTextBoundaryFinder::BoundaryType type,
    const QChar *chars,
    qsizetype length,
    unsigned char *buffer,
    qsizetype bufferSize) {
  return new QTextBoundaryFinder(type, chars, length, buffer, bufferSize);
}

//  QTextBoundaryFinder::QTextBoundaryFinder(BoundaryType type, QStringView
//      str, unsigned char *buffer, qsizetype bufferSize)
extern "C" Q_DECL_EXPORT
QTextBoundaryFinder *ritual_ZN19QTextBoundaryFinderC1ENS_12BoundaryTypeE11QStringViewPhx(
    QTextBoundaryFinder::BoundaryType type,
    const QString *str,
    unsigned char *buffer,
    qsizetype bufferSize) {
  return new QTextBoundaryFinder(
      type,
      QStringView(*str),
      buffer,
      bufferSize);
}

//  bool QTextBoundaryFinder::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextBoundaryFinder7isValidEv(
    const QTextBoundaryFinder *self) {
  return self->isValid();
}

//  BoundaryType QTextBoundaryFinder::type() const
extern "C" Q_DECL_EXPORT
QTextBoundaryFinder::BoundaryType ritual_ZNK19QTextBoundaryFinder4typeEv(
    const QTextBoundaryFinder *self) {
  return self->type();
}

//  QString QTextBoundaryFinder::string() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QTextBoundaryFinder6stringEv(
    const QTextBoundaryFinder *self) {
  return new QString(self->string());
}

//  void QTextBoundaryFinder::toStart()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextBoundaryFinder7toStartEv(QTextBoundaryFinder *self) {
  self->toStart();
}

//  void QTextBoundaryFinder::toEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextBoundaryFinder5toEndEv(QTextBoundaryFinder *self) {
  self->toEnd();
}

//  qsizetype QTextBoundaryFinder::position() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK19QTextBoundaryFinder8positionEv(
    const QTextBoundaryFinder *self) {
  return self->position();
}

//  void QTextBoundaryFinder::setPosition(qsizetype position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextBoundaryFinder11setPositionEx(
    QTextBoundaryFinder *self,
    qsizetype position) {
  self->setPosition(position);
}

//  qsizetype QTextBoundaryFinder::toNextBoundary()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QTextBoundaryFinder14toNextBoundaryEv(
    QTextBoundaryFinder *self) {
  return self->toNextBoundary();
}

//  qsizetype QTextBoundaryFinder::toPreviousBoundary()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QTextBoundaryFinder18toPreviousBoundaryEv(
    QTextBoundaryFinder *self) {
  return self->toPreviousBoundary();
}

//  bool QTextBoundaryFinder::isAtBoundary() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextBoundaryFinder12isAtBoundaryEv(
    const QTextBoundaryFinder *self) {
  return self->isAtBoundary();
}

//  BoundaryReasons QTextBoundaryFinder::boundaryReasons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QTextBoundaryFinder15boundaryReasonsEv(
    const QTextBoundaryFinder *self) {
  return static_cast<int>(self->boundaryReasons().toInt());
}
