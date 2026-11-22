//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qglyphrun.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qglyphrun.h>
#include <QtGui/qrawfont.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QGlyphRun::QGlyphRun()
extern "C" Q_DECL_EXPORT
QGlyphRun *ritual_ZN9QGlyphRunC1Ev() {
  return new QGlyphRun();
}

//  QGlyphRun::QGlyphRun(const QGlyphRun &other)
extern "C" Q_DECL_EXPORT
QGlyphRun *ritual_ZN9QGlyphRunC1ERKS_(const QGlyphRun *other) {
  return new QGlyphRun(*other);
}

//  QGlyphRun::~QGlyphRun()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRunD1Ev(QGlyphRun *self) {
  delete self;
}

//  QRawFont QGlyphRun::rawFont() const
extern "C" Q_DECL_EXPORT
QRawFont *ritual_ZNK9QGlyphRun7rawFontEv(const QGlyphRun *self) {
  return new QRawFont(self->rawFont());
}

//  void QGlyphRun::setRawFont(const QRawFont &rawFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun10setRawFontERK8QRawFont(
    QGlyphRun *self,
    const QRawFont *rawFont) {
  self->setRawFont(*rawFont);
}

//  QList<QPointF> QGlyphRun::positions() const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK9QGlyphRun9positionsEv(const QGlyphRun *self) {
  return new QList<QPointF>(self->positions());
}

//  void QGlyphRun::setPositions(const QList<QPointF> &positions)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun12setPositionsERK5QListI7QPointFE(
    QGlyphRun *self,
    const QList<QPointF> *positions) {
  self->setPositions(*positions);
}

//  void QGlyphRun::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun5clearEv(QGlyphRun *self) {
  self->clear();
}

//  bool QGlyphRun::operator==(const QGlyphRun &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGlyphRuneqERKS_(
    const QGlyphRun *self,
    const QGlyphRun *other) {
  return self->operator==(*other);
}

//  bool QGlyphRun::operator!=(const QGlyphRun &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGlyphRunneERKS_(
    const QGlyphRun *self,
    const QGlyphRun *other) {
  return self->operator!=(*other);
}

//  void QGlyphRun::setOverline(bool overline)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun11setOverlineEb(QGlyphRun *self, bool overline) {
  self->setOverline(overline);
}

//  bool QGlyphRun::overline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGlyphRun8overlineEv(const QGlyphRun *self) {
  return self->overline();
}

//  void QGlyphRun::setUnderline(bool underline)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun12setUnderlineEb(QGlyphRun *self, bool underline) {
  self->setUnderline(underline);
}

//  bool QGlyphRun::underline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGlyphRun9underlineEv(const QGlyphRun *self) {
  return self->underline();
}

//  void QGlyphRun::setStrikeOut(bool strikeOut)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun12setStrikeOutEb(QGlyphRun *self, bool strikeOut) {
  self->setStrikeOut(strikeOut);
}

//  bool QGlyphRun::strikeOut() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGlyphRun9strikeOutEv(const QGlyphRun *self) {
  return self->strikeOut();
}

//  void QGlyphRun::setRightToLeft(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun14setRightToLeftEb(QGlyphRun *self, bool on) {
  self->setRightToLeft(on);
}

//  bool QGlyphRun::isRightToLeft() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGlyphRun13isRightToLeftEv(const QGlyphRun *self) {
  return self->isRightToLeft();
}

//  void QGlyphRun::setFlag(GlyphRunFlag flag, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun7setFlagENS_12GlyphRunFlagEb(
    QGlyphRun *self,
    QGlyphRun::GlyphRunFlag flag,
    bool enabled) {
  self->setFlag(flag, enabled);
}

//  void QGlyphRun::setFlags(GlyphRunFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun8setFlagsE6QFlagsINS_12GlyphRunFlagEE(
    QGlyphRun *self,
    int flags) {
  self->setFlags(QFlags<QGlyphRun::GlyphRunFlag>::fromInt(flags));
}

//  GlyphRunFlags QGlyphRun::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QGlyphRun5flagsEv(const QGlyphRun *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QGlyphRun::setBoundingRect(const QRectF &boundingRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun15setBoundingRectERK6QRectF(
    QGlyphRun *self,
    const QRectF *boundingRect) {
  self->setBoundingRect(*boundingRect);
}

//  QRectF QGlyphRun::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK9QGlyphRun12boundingRectEv(const QGlyphRun *self) {
  return new QRectF(self->boundingRect());
}

//  void QGlyphRun::setSourceString(const QString &sourceString)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGlyphRun15setSourceStringERK7QString(
    QGlyphRun *self,
    const QString *sourceString) {
  self->setSourceString(*sourceString);
}

//  QString QGlyphRun::sourceString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QGlyphRun12sourceStringEv(const QGlyphRun *self) {
  return new QString(self->sourceString());
}

//  bool QGlyphRun::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGlyphRun7isEmptyEv(const QGlyphRun *self) {
  return self->isEmpty();
}

//  QList<QGlyphRun>::QList()
extern "C" Q_DECL_EXPORT
QList<QGlyphRun> *ritual_list_make_QGlyphRun() {
  return new QList<QGlyphRun>();
}

//  void QList<QGlyphRun>::append(const QGlyphRun &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGlyphRun(
    QList<QGlyphRun> *self,
    const QGlyphRun *element) {
  self->append(*element);
}

//  qsizetype QList<QGlyphRun>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGlyphRun(const QList<QGlyphRun> *self) {
  return self->size();
}

//  const QGlyphRun &QList<QGlyphRun>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGlyphRun *ritual_list_at_QGlyphRun(
    const QList<QGlyphRun> *self,
    long long index) {
  return new QGlyphRun(self->at(index));
}

//  QList<QGlyphRun>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGlyphRun(QList<QGlyphRun> *self) {
  delete self;
}
