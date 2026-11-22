//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qabstracttextdocumentlayout.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtextobject.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QAbstractTextDocumentLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QAbstractTextDocumentLayout10metaObjectEv(
    const QAbstractTextDocumentLayout *self) {
  return self->metaObject();
}

//  QString QAbstractTextDocumentLayout::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QAbstractTextDocumentLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractTextDocumentLayout::tr(s, c, n));
}

//  QAbstractTextDocumentLayout::~QAbstractTextDocumentLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayoutD1Ev(
    QAbstractTextDocumentLayout *self) {
  delete self;
}

//  void QAbstractTextDocumentLayout::draw(QPainter *painter, const
//      PaintContext &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout4drawEP8QPainterRKNS_12PaintContextE(
    QAbstractTextDocumentLayout *self,
    QPainter *painter,
    const QAbstractTextDocumentLayout::PaintContext *context) {
  self->draw(painter, *context);
}

//  int QAbstractTextDocumentLayout::hitTest(const QPointF &point,
//      Qt::HitTestAccuracy accuracy) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QAbstractTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QAbstractTextDocumentLayout *self,
    const QPointF *point,
    Qt::HitTestAccuracy accuracy) {
  return self->hitTest(*point, accuracy);
}

//  QString QAbstractTextDocumentLayout::anchorAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QAbstractTextDocumentLayout8anchorAtERK7QPointF(
    const QAbstractTextDocumentLayout *self,
    const QPointF *pos) {
  return new QString(self->anchorAt(*pos));
}

//  QString QAbstractTextDocumentLayout::imageAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QAbstractTextDocumentLayout7imageAtERK7QPointF(
    const QAbstractTextDocumentLayout *self,
    const QPointF *pos) {
  return new QString(self->imageAt(*pos));
}

//  QTextFormat QAbstractTextDocumentLayout::formatAt(const QPointF &pos)
//      const
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZNK27QAbstractTextDocumentLayout8formatAtERK7QPointF(
    const QAbstractTextDocumentLayout *self,
    const QPointF *pos) {
  return new QTextFormat(self->formatAt(*pos));
}

//  QTextBlock QAbstractTextDocumentLayout::blockWithMarkerAt(const QPointF
//      &pos) const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK27QAbstractTextDocumentLayout17blockWithMarkerAtERK7QPointF(
    const QAbstractTextDocumentLayout *self,
    const QPointF *pos) {
  return new QTextBlock(self->blockWithMarkerAt(*pos));
}

//  int QAbstractTextDocumentLayout::pageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QAbstractTextDocumentLayout9pageCountEv(
    const QAbstractTextDocumentLayout *self) {
  return self->pageCount();
}

//  QSizeF QAbstractTextDocumentLayout::documentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK27QAbstractTextDocumentLayout12documentSizeEv(
    const QAbstractTextDocumentLayout *self) {
  return new QSizeF(self->documentSize());
}

//  QRectF QAbstractTextDocumentLayout::frameBoundingRect(QTextFrame *frame)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK27QAbstractTextDocumentLayout17frameBoundingRectEP10QTextFrame(
    const QAbstractTextDocumentLayout *self,
    QTextFrame *frame) {
  return new QRectF(self->frameBoundingRect(frame));
}

//  QRectF QAbstractTextDocumentLayout::blockBoundingRect(const QTextBlock
//      &block) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK27QAbstractTextDocumentLayout17blockBoundingRectERK10QTextBlock(
    const QAbstractTextDocumentLayout *self,
    const QTextBlock *block) {
  return new QRectF(self->blockBoundingRect(*block));
}

//  void QAbstractTextDocumentLayout::setPaintDevice(QPaintDevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout14setPaintDeviceEP12QPaintDevice(
    QAbstractTextDocumentLayout *self,
    QPaintDevice *device) {
  self->setPaintDevice(device);
}

//  QPaintDevice *QAbstractTextDocumentLayout::paintDevice() const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZNK27QAbstractTextDocumentLayout11paintDeviceEv(
    const QAbstractTextDocumentLayout *self) {
  return self->paintDevice();
}

//  QTextDocument *QAbstractTextDocumentLayout::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK27QAbstractTextDocumentLayout8documentEv(
    const QAbstractTextDocumentLayout *self) {
  return self->document();
}

//  void QAbstractTextDocumentLayout::registerHandler(int objectType, QObject
//      *component)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout15registerHandlerEiP7QObject(
    QAbstractTextDocumentLayout *self,
    int objectType,
    QObject *component) {
  self->registerHandler(objectType, component);
}

//  void QAbstractTextDocumentLayout::unregisterHandler(int objectType,
//      QObject *component)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractTextDocumentLayout17unregisterHandlerEiP7QObject(
    QAbstractTextDocumentLayout *self,
    int objectType,
    QObject *component) {
  self->unregisterHandler(objectType, component);
}

//  QTextObjectInterface *QAbstractTextDocumentLayout::handlerForObject(int
//      objectType) const
extern "C" Q_DECL_EXPORT
QTextObjectInterface *ritual_ZNK27QAbstractTextDocumentLayout16handlerForObjectEi(
    const QAbstractTextDocumentLayout *self,
    int objectType) {
  return self->handlerForObject(objectType);
}
