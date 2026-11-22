//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextobject.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtextcursor.h>

//  const QMetaObject *QTextFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QTextFrame10metaObjectEv(
    const QTextFrame *self) {
  return self->metaObject();
}

//  QString QTextFrame::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QTextFrame2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextFrame::tr(s, c, n));
}

//  QTextFrame::QTextFrame(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZN10QTextFrameC1EP13QTextDocument(QTextDocument *doc) {
  return new QTextFrame(doc);
}

//  QTextFrame::~QTextFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextFrameD1Ev(QTextFrame *self) {
  delete self;
}

//  void QTextFrame::setFrameFormat(const QTextFrameFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextFrame14setFrameFormatERK16QTextFrameFormat(
    QTextFrame *self,
    const QTextFrameFormat *format) {
  self->setFrameFormat(*format);
}

//  QTextFrameFormat QTextFrame::frameFormat() const
extern "C" Q_DECL_EXPORT
QTextFrameFormat *ritual_ZNK10QTextFrame11frameFormatEv(
    const QTextFrame *self) {
  return new QTextFrameFormat(self->frameFormat());
}

//  QTextCursor QTextFrame::firstCursorPosition() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK10QTextFrame19firstCursorPositionEv(
    const QTextFrame *self) {
  return new QTextCursor(self->firstCursorPosition());
}

//  QTextCursor QTextFrame::lastCursorPosition() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK10QTextFrame18lastCursorPositionEv(
    const QTextFrame *self) {
  return new QTextCursor(self->lastCursorPosition());
}

//  int QTextFrame::firstPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextFrame13firstPositionEv(const QTextFrame *self) {
  return self->firstPosition();
}

//  int QTextFrame::lastPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextFrame12lastPositionEv(const QTextFrame *self) {
  return self->lastPosition();
}

//  QTextFrameLayoutData *QTextFrame::layoutData() const
extern "C" Q_DECL_EXPORT
QTextFrameLayoutData *ritual_ZNK10QTextFrame10layoutDataEv(
    const QTextFrame *self) {
  return self->layoutData();
}

//  void QTextFrame::setLayoutData(QTextFrameLayoutData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextFrame13setLayoutDataEP20QTextFrameLayoutData(
    QTextFrame *self,
    QTextFrameLayoutData *data) {
  self->setLayoutData(data);
}

//  QTextFrame *QTextFrame::parentFrame() const
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZNK10QTextFrame11parentFrameEv(const QTextFrame *self) {
  return self->parentFrame();
}

//  iterator QTextFrame::begin() const
extern "C" Q_DECL_EXPORT
QTextFrame::iterator *ritual_ZNK10QTextFrame5beginEv(
    const QTextFrame *self) {
  return new QTextFrame::iterator(self->begin());
}

//  iterator QTextFrame::end() const
extern "C" Q_DECL_EXPORT
QTextFrame::iterator *ritual_ZNK10QTextFrame3endEv(const QTextFrame *self) {
  return new QTextFrame::iterator(self->end());
}
