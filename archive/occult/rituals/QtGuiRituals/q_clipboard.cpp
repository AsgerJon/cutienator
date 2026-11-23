//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qclipboard.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qclipboard.h>
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtGui/qpixmap.h>

//  const QMetaObject *QClipboard::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QClipboard10metaObjectEv(
    const QClipboard *self) {
  return self->metaObject();
}

//  QString QClipboard::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QClipboard2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QClipboard::tr(s, c, n));
}

//  QClipboard::QClipboard(QObject *parent)
extern "C" Q_DECL_EXPORT
QClipboard *ritual_ZN10QClipboardC1EP7QObject(QObject *parent) {
  return new QClipboard(parent);
}

//  QClipboard::~QClipboard()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QClipboardD1Ev(QClipboard *self) {
  delete self;
}

//  void QClipboard::clear(Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QClipboard5clearENS_4ModeE(
    QClipboard *self,
    QClipboard::Mode mode) {
  self->clear(mode);
}

//  bool QClipboard::supportsSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QClipboard17supportsSelectionEv(const QClipboard *self) {
  return self->supportsSelection();
}

//  bool QClipboard::supportsFindBuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QClipboard18supportsFindBufferEv(const QClipboard *self) {
  return self->supportsFindBuffer();
}

//  bool QClipboard::ownsSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QClipboard13ownsSelectionEv(const QClipboard *self) {
  return self->ownsSelection();
}

//  bool QClipboard::ownsClipboard() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QClipboard13ownsClipboardEv(const QClipboard *self) {
  return self->ownsClipboard();
}

//  bool QClipboard::ownsFindBuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QClipboard14ownsFindBufferEv(const QClipboard *self) {
  return self->ownsFindBuffer();
}

//  QString QClipboard::text(Mode mode) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QClipboard4textENS_4ModeE(
    const QClipboard *self,
    QClipboard::Mode mode) {
  return new QString(self->text(mode));
}

//  void QClipboard::setText(const QString &a0, Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QClipboard7setTextERK7QStringNS_4ModeE(
    QClipboard *self,
    const QString *a0,
    QClipboard::Mode mode) {
  self->setText(*a0, mode);
}

//  const QMimeData *QClipboard::mimeData(Mode mode) const
extern "C" Q_DECL_EXPORT
const QMimeData *ritual_ZNK10QClipboard8mimeDataENS_4ModeE(
    const QClipboard *self,
    QClipboard::Mode mode) {
  return self->mimeData(mode);
}

//  void QClipboard::setMimeData(QMimeData *data, Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QClipboard11setMimeDataEP9QMimeDataNS_4ModeE(
    QClipboard *self,
    QMimeData *data,
    QClipboard::Mode mode) {
  self->setMimeData(data, mode);
}

//  QImage QClipboard::image(Mode mode) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK10QClipboard5imageENS_4ModeE(
    const QClipboard *self,
    QClipboard::Mode mode) {
  return new QImage(self->image(mode));
}

//  QPixmap QClipboard::pixmap(Mode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK10QClipboard6pixmapENS_4ModeE(
    const QClipboard *self,
    QClipboard::Mode mode) {
  return new QPixmap(self->pixmap(mode));
}

//  void QClipboard::setImage(const QImage &a0, Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QClipboard8setImageERK6QImageNS_4ModeE(
    QClipboard *self,
    const QImage *a0,
    QClipboard::Mode mode) {
  self->setImage(*a0, mode);
}

//  void QClipboard::setPixmap(const QPixmap &a0, Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QClipboard9setPixmapERK7QPixmapNS_4ModeE(
    QClipboard *self,
    const QPixmap *a0,
    QClipboard::Mode mode) {
  self->setPixmap(*a0, mode);
}

//  bool QClipboard::supportsMode(Mode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QClipboard12supportsModeENS_4ModeE(
    const QClipboard *self,
    QClipboard::Mode mode) {
  return self->supportsMode(mode);
}

//  bool QClipboard::ownsMode(Mode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QClipboard8ownsModeENS_4ModeE(
    const QClipboard *self,
    QClipboard::Mode mode) {
  return self->ownsMode(mode);
}

//  void QClipboard::emitChanged(Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QClipboard11emitChangedENS_4ModeE(
    QClipboard *self,
    QClipboard::Mode mode) {
  self->emitChanged(mode);
}
