//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtexttable.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtexttable.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextobject.h>

//  QTextTableCell::QTextTableCell()
extern "C" Q_DECL_EXPORT
QTextTableCell *ritual_ZN14QTextTableCellC1Ev() {
  return new QTextTableCell();
}

//  QTextTableCell::~QTextTableCell()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTextTableCellD1Ev(QTextTableCell *self) {
  delete self;
}

//  QTextTableCell::QTextTableCell(const QTextTableCell &o)
extern "C" Q_DECL_EXPORT
QTextTableCell *ritual_ZN14QTextTableCellC1ERKS_(const QTextTableCell *o) {
  return new QTextTableCell(*o);
}

//  QTextTableCell &QTextTableCell::operator=(const QTextTableCell &o)
extern "C" Q_DECL_EXPORT
QTextTableCell *ritual_ZN14QTextTableCellaSERKS_(
    QTextTableCell *self,
    const QTextTableCell *o) {
  return &(self->operator=(*o));
}

//  void QTextTableCell::setFormat(const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTextTableCell9setFormatERK15QTextCharFormat(
    QTextTableCell *self,
    const QTextCharFormat *format) {
  self->setFormat(*format);
}

//  QTextCharFormat QTextTableCell::format() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK14QTextTableCell6formatEv(
    const QTextTableCell *self) {
  return new QTextCharFormat(self->format());
}

//  int QTextTableCell::row() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QTextTableCell3rowEv(const QTextTableCell *self) {
  return self->row();
}

//  int QTextTableCell::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QTextTableCell6columnEv(const QTextTableCell *self) {
  return self->column();
}

//  int QTextTableCell::rowSpan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QTextTableCell7rowSpanEv(const QTextTableCell *self) {
  return self->rowSpan();
}

//  int QTextTableCell::columnSpan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QTextTableCell10columnSpanEv(const QTextTableCell *self) {
  return self->columnSpan();
}

//  bool QTextTableCell::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QTextTableCell7isValidEv(const QTextTableCell *self) {
  return self->isValid();
}

//  QTextCursor QTextTableCell::firstCursorPosition() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK14QTextTableCell19firstCursorPositionEv(
    const QTextTableCell *self) {
  return new QTextCursor(self->firstCursorPosition());
}

//  QTextCursor QTextTableCell::lastCursorPosition() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK14QTextTableCell18lastCursorPositionEv(
    const QTextTableCell *self) {
  return new QTextCursor(self->lastCursorPosition());
}

//  int QTextTableCell::firstPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QTextTableCell13firstPositionEv(const QTextTableCell *self) {
  return self->firstPosition();
}

//  int QTextTableCell::lastPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QTextTableCell12lastPositionEv(const QTextTableCell *self) {
  return self->lastPosition();
}

//  bool QTextTableCell::operator==(const QTextTableCell &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QTextTableCelleqERKS_(
    const QTextTableCell *self,
    const QTextTableCell *other) {
  return self->operator==(*other);
}

//  bool QTextTableCell::operator!=(const QTextTableCell &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QTextTableCellneERKS_(
    const QTextTableCell *self,
    const QTextTableCell *other) {
  return self->operator!=(*other);
}

//  QTextFrame::iterator QTextTableCell::begin() const
extern "C" Q_DECL_EXPORT
QTextFrame::iterator *ritual_ZNK14QTextTableCell5beginEv(
    const QTextTableCell *self) {
  return new QTextFrame::iterator(self->begin());
}

//  QTextFrame::iterator QTextTableCell::end() const
extern "C" Q_DECL_EXPORT
QTextFrame::iterator *ritual_ZNK14QTextTableCell3endEv(
    const QTextTableCell *self) {
  return new QTextFrame::iterator(self->end());
}

//  int QTextTableCell::tableCellFormatIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QTextTableCell20tableCellFormatIndexEv(
    const QTextTableCell *self) {
  return self->tableCellFormatIndex();
}

//  QTextTableCell::QTextTableCell(const QTextTable *t, int f)
extern "C" Q_DECL_EXPORT
QTextTableCell *ritual_ZN14QTextTableCellC1EPK10QTextTablei(
    const QTextTable *t,
    int f) {
  return new QTextTableCell(t, f);
}
