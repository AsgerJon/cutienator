//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qxpmhandler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_IMAGEFORMAT_XPM)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qxpmhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qvariant.h>

//  bool QXpmHandler::canRead() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QXpmHandler7canReadEv(const QXpmHandler *self) {
  return self->canRead();
}

//  bool QXpmHandler::read(QImage *image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QXpmHandler4readEP6QImage(QXpmHandler *self, QImage *image) {
  return self->read(image);
}

//  bool QXpmHandler::write(const QImage &image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QXpmHandler5writeERK6QImage(
    QXpmHandler *self,
    const QImage *image) {
  return self->write(*image);
}

//  QVariant QXpmHandler::option(ImageOption option) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QXpmHandler6optionEN15QImageIOHandler11ImageOptionE(
    const QXpmHandler *self,
    QImageIOHandler::ImageOption option) {
  return new QVariant(self->option(option));
}

//  void QXpmHandler::setOption(ImageOption option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QXpmHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant(
    QXpmHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->setOption(option, *value);
}

//  bool QXpmHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QXpmHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QXpmHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->supportsOption(option);
}

#endif  // !defined(QT_NO_IMAGEFORMAT_XPM)
