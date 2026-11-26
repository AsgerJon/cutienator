//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qimagepixmapcleanuphooks_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qimagepixmapcleanuphooks_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtGui/qpixmap.h>

//  QImagePixmapCleanupHooks *QImagePixmapCleanupHooks::instance()
extern "C" Q_DECL_EXPORT
QImagePixmapCleanupHooks *ritual_ZN24QImagePixmapCleanupHooks8instanceEv() {
  return QImagePixmapCleanupHooks::instance();
}

//  void QImagePixmapCleanupHooks::enableCleanupHooks(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks18enableCleanupHooksERK6QImage(
    const QImage *image) {
  QImagePixmapCleanupHooks::enableCleanupHooks(*image);
}

//  void QImagePixmapCleanupHooks::enableCleanupHooks(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks18enableCleanupHooksERK7QPixmap(
    const QPixmap *pixmap) {
  QImagePixmapCleanupHooks::enableCleanupHooks(*pixmap);
}

//  void QImagePixmapCleanupHooks::enableCleanupHooks(QPlatformPixmap
//      *handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks18enableCleanupHooksEP15QPlatformPixmap(
    QPlatformPixmap *handle) {
  QImagePixmapCleanupHooks::enableCleanupHooks(handle);
}

//  bool QImagePixmapCleanupHooks::isImageCached(const QImage &image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QImagePixmapCleanupHooks13isImageCachedERK6QImage(
    const QImage *image) {
  return QImagePixmapCleanupHooks::isImageCached(*image);
}

//  bool QImagePixmapCleanupHooks::isPixmapCached(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QImagePixmapCleanupHooks14isPixmapCachedERK7QPixmap(
    const QPixmap *pixmap) {
  return QImagePixmapCleanupHooks::isPixmapCached(*pixmap);
}

//  void QImagePixmapCleanupHooks::addPlatformPixmapModificationHook(_qt_pixm
//      ap_cleanup_hook_pmd a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks33addPlatformPixmapModificationHookEPFvP15QPlatformPixmapE(
    QImagePixmapCleanupHooks *self,
    void *a0) {
  self->addPlatformPixmapModificationHook(
      reinterpret_cast<_qt_pixmap_cleanup_hook_pmd>(a0));
}

//  void QImagePixmapCleanupHooks::addPlatformPixmapDestructionHook(_qt_pixma
//      p_cleanup_hook_pmd a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks32addPlatformPixmapDestructionHookEPFvP15QPlatformPixmapE(
    QImagePixmapCleanupHooks *self,
    void *a0) {
  self->addPlatformPixmapDestructionHook(
      reinterpret_cast<_qt_pixmap_cleanup_hook_pmd>(a0));
}

//  void QImagePixmapCleanupHooks::addImageHook(_qt_image_cleanup_hook_64 a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks12addImageHookEPFvxE(
    QImagePixmapCleanupHooks *self,
    void *a0) {
  self->addImageHook(reinterpret_cast<_qt_image_cleanup_hook_64>(a0));
}

//  void QImagePixmapCleanupHooks::removePlatformPixmapModificationHook(_qt_p
//      ixmap_cleanup_hook_pmd a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks36removePlatformPixmapModificationHookEPFvP15QPlatformPixmapE(
    QImagePixmapCleanupHooks *self,
    void *a0) {
  self->removePlatformPixmapModificationHook(
      reinterpret_cast<_qt_pixmap_cleanup_hook_pmd>(a0));
}

//  void QImagePixmapCleanupHooks::removePlatformPixmapDestructionHook(_qt_pi
//      xmap_cleanup_hook_pmd a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks35removePlatformPixmapDestructionHookEPFvP15QPlatformPixmapE(
    QImagePixmapCleanupHooks *self,
    void *a0) {
  self->removePlatformPixmapDestructionHook(
      reinterpret_cast<_qt_pixmap_cleanup_hook_pmd>(a0));
}

//  void QImagePixmapCleanupHooks::removeImageHook(_qt_image_cleanup_hook_64
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks15removeImageHookEPFvxE(
    QImagePixmapCleanupHooks *self,
    void *a0) {
  self->removeImageHook(reinterpret_cast<_qt_image_cleanup_hook_64>(a0));
}

//  void QImagePixmapCleanupHooks::executePlatformPixmapModificationHooks(QPl
//      atformPixmap *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks38executePlatformPixmapModificationHooksEP15QPlatformPixmap(
    QPlatformPixmap *a0) {
  QImagePixmapCleanupHooks::executePlatformPixmapModificationHooks(a0);
}

//  void QImagePixmapCleanupHooks::executePlatformPixmapDestructionHooks(QPla
//      tformPixmap *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks37executePlatformPixmapDestructionHooksEP15QPlatformPixmap(
    QPlatformPixmap *a0) {
  QImagePixmapCleanupHooks::executePlatformPixmapDestructionHooks(a0);
}

//  void QImagePixmapCleanupHooks::executeImageHooks(qint64 key)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooks17executeImageHooksEx(qint64 key) {
  QImagePixmapCleanupHooks::executeImageHooks(key);
}

//  QImagePixmapCleanupHooks::~QImagePixmapCleanupHooks()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QImagePixmapCleanupHooksD1Ev(
    QImagePixmapCleanupHooks *self) {
  delete self;
}
