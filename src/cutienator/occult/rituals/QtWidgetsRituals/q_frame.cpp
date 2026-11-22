//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qframe.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qframe.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QFrame10metaObjectEv(const QFrame *self) {
  return self->metaObject();
}

//  QString QFrame::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QFrame2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QFrame::tr(s, c, n));
}

//  QFrame::QFrame(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QFrame *ritual_ZN6QFrameC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new QFrame(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QFrame::~QFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrameD1Ev(QFrame *self) {
  delete self;
}

//  int QFrame::frameStyle() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFrame10frameStyleEv(const QFrame *self) {
  return self->frameStyle();
}

//  void QFrame::setFrameStyle(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame13setFrameStyleEi(QFrame *self, int a0) {
  self->setFrameStyle(a0);
}

//  int QFrame::frameWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFrame10frameWidthEv(const QFrame *self) {
  return self->frameWidth();
}

//  QSize QFrame::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6QFrame8sizeHintEv(const QFrame *self) {
  return new QSize(self->sizeHint());
}

//  Shape QFrame::frameShape() const
extern "C" Q_DECL_EXPORT
QFrame::Shape ritual_ZNK6QFrame10frameShapeEv(const QFrame *self) {
  return self->frameShape();
}

//  void QFrame::setFrameShape(Shape a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame13setFrameShapeENS_5ShapeE(
    QFrame *self,
    QFrame::Shape a0) {
  self->setFrameShape(a0);
}

//  Shadow QFrame::frameShadow() const
extern "C" Q_DECL_EXPORT
QFrame::Shadow ritual_ZNK6QFrame11frameShadowEv(const QFrame *self) {
  return self->frameShadow();
}

//  void QFrame::setFrameShadow(Shadow a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame14setFrameShadowENS_6ShadowE(
    QFrame *self,
    QFrame::Shadow a0) {
  self->setFrameShadow(a0);
}

//  int QFrame::lineWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFrame9lineWidthEv(const QFrame *self) {
  return self->lineWidth();
}

//  void QFrame::setLineWidth(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame12setLineWidthEi(QFrame *self, int a0) {
  self->setLineWidth(a0);
}

//  int QFrame::midLineWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFrame12midLineWidthEv(const QFrame *self) {
  return self->midLineWidth();
}

//  void QFrame::setMidLineWidth(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame15setMidLineWidthEi(QFrame *self, int a0) {
  self->setMidLineWidth(a0);
}

//  QRect QFrame::frameRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK6QFrame9frameRectEv(const QFrame *self) {
  return new QRect(self->frameRect());
}

//  void QFrame::setFrameRect(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFrame12setFrameRectERK5QRect(QFrame *self, const QRect *a0) {
  self->setFrameRect(*a0);
}
