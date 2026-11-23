//  Written by dev_tooling.RitualGenerator from the records of QtGui/qicon.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qicon.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>

//  QIcon::QIcon()
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN5QIconC1Ev() {
  return new QIcon();
}

//  QIcon::QIcon(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN5QIconC1ERK7QPixmap(const QPixmap *pixmap) {
  return new QIcon(*pixmap);
}

//  QIcon::QIcon(const QIcon &other)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN5QIconC1ERKS_(const QIcon *other) {
  return new QIcon(*other);
}

//  QIcon::QIcon(const QString &fileName)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN5QIconC1ERK7QString(const QString *fileName) {
  return new QIcon(*fileName);
}

//  QIcon::QIcon(QIconEngine *engine)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN5QIconC1EP11QIconEngine(QIconEngine *engine) {
  return new QIcon(engine);
}

//  QIcon::~QIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QIconD1Ev(QIcon *self) {
  delete self;
}

//  QVariant QIcon::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK5QIconcv8QVariantEv(const QIcon *self) {
  return new QVariant(self->operator QVariant());
}

//  QPixmap QIcon::pixmap(const QSize &size, Mode mode, State state) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK5QIcon6pixmapERK5QSizeNS_4ModeENS_5StateE(
    const QIcon *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(*size, mode, state));
}

//  QPixmap QIcon::pixmap(int w, int h, Mode mode, State state) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK5QIcon6pixmapEiiNS_4ModeENS_5StateE(
    const QIcon *self,
    int w,
    int h,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(w, h, mode, state));
}

//  QPixmap QIcon::pixmap(int extent, Mode mode, State state) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK5QIcon6pixmapEiNS_4ModeENS_5StateE(
    const QIcon *self,
    int extent,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(extent, mode, state));
}

//  QPixmap QIcon::pixmap(const QSize &size, qreal devicePixelRatio, Mode
//      mode, State state) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK5QIcon6pixmapERK5QSizedNS_4ModeENS_5StateE(
    const QIcon *self,
    const QSize *size,
    qreal devicePixelRatio,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(*size, devicePixelRatio, mode, state));
}

//  QPixmap QIcon::pixmap(QWindow *window, const QSize &size, Mode mode,
//      State state) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK5QIcon6pixmapEP7QWindowRK5QSizeNS_4ModeENS_5StateE(
    const QIcon *self,
    QWindow *window,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(window, *size, mode, state));
}

//  QSize QIcon::actualSize(const QSize &size, Mode mode, State state) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QIcon10actualSizeERK5QSizeNS_4ModeENS_5StateE(
    const QIcon *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->actualSize(*size, mode, state));
}

//  QSize QIcon::actualSize(QWindow *window, const QSize &size, Mode mode,
//      State state) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QIcon10actualSizeEP7QWindowRK5QSizeNS_4ModeENS_5StateE(
    const QIcon *self,
    QWindow *window,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->actualSize(window, *size, mode, state));
}

//  QString QIcon::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QIcon4nameEv(const QIcon *self) {
  return new QString(self->name());
}

//  void QIcon::paint(QPainter *painter, const QRect &rect, Qt::Alignment
//      alignment, Mode mode, State state) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK5QIcon5paintEP8QPainterRK5QRect6QFlagsIN2Qt13AlignmentFlagEENS_4ModeENS_5StateE(
    const QIcon *self,
    QPainter *painter,
    const QRect *rect,
    int alignment,
    QIcon::Mode mode,
    QIcon::State state) {
  self->paint(
      painter,
      *rect,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment),
      mode,
      state);
}

//  void QIcon::paint(QPainter *painter, int x, int y, int w, int h,
//      Qt::Alignment alignment, Mode mode, State state) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK5QIcon5paintEP8QPainteriiii6QFlagsIN2Qt13AlignmentFlagEENS_4ModeENS_5StateE(
    const QIcon *self,
    QPainter *painter,
    int x,
    int y,
    int w,
    int h,
    int alignment,
    QIcon::Mode mode,
    QIcon::State state) {
  self->paint(
      painter,
      x,
      y,
      w,
      h,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment),
      mode,
      state);
}

//  bool QIcon::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QIcon6isNullEv(const QIcon *self) {
  return self->isNull();
}

//  bool QIcon::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QIcon10isDetachedEv(const QIcon *self) {
  return self->isDetached();
}

//  void QIcon::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QIcon6detachEv(QIcon *self) {
  self->detach();
}

//  qint64 QIcon::cacheKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK5QIcon8cacheKeyEv(const QIcon *self) {
  return self->cacheKey();
}

//  void QIcon::addPixmap(const QPixmap &pixmap, Mode mode, State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QIcon9addPixmapERK7QPixmapNS_4ModeENS_5StateE(
    QIcon *self,
    const QPixmap *pixmap,
    QIcon::Mode mode,
    QIcon::State state) {
  self->addPixmap(*pixmap, mode, state);
}

//  void QIcon::addFile(const QString &fileName, const QSize &size, Mode
//      mode, State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QIcon7addFileERK7QStringRK5QSizeNS_4ModeENS_5StateE(
    QIcon *self,
    const QString *fileName,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  self->addFile(*fileName, *size, mode, state);
}

//  QList<QSize> QIcon::availableSizes(Mode mode, State state) const
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZNK5QIcon14availableSizesENS_4ModeENS_5StateE(
    const QIcon *self,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QList<QSize>(self->availableSizes(mode, state));
}

//  void QIcon::setIsMask(bool isMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QIcon9setIsMaskEb(QIcon *self, bool isMask) {
  self->setIsMask(isMask);
}

//  bool QIcon::isMask() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QIcon6isMaskEv(const QIcon *self) {
  return self->isMask();
}

//  QIcon QIcon::fromTheme(const QString &name)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN5QIcon9fromThemeERK7QString(const QString *name) {
  return new QIcon(QIcon::fromTheme(*name));
}

//  QIcon QIcon::fromTheme(const QString &name, const QIcon &fallback)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN5QIcon9fromThemeERK7QStringRKS_(
    const QString *name,
    const QIcon *fallback) {
  return new QIcon(QIcon::fromTheme(*name, *fallback));
}

//  bool QIcon::hasThemeIcon(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QIcon12hasThemeIconERK7QString(const QString *name) {
  return QIcon::hasThemeIcon(*name);
}

//  QIcon QIcon::fromTheme(ThemeIcon icon)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN5QIcon9fromThemeENS_9ThemeIconE(QIcon::ThemeIcon icon) {
  return new QIcon(QIcon::fromTheme(icon));
}

//  QIcon QIcon::fromTheme(ThemeIcon icon, const QIcon &fallback)
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZN5QIcon9fromThemeENS_9ThemeIconERKS_(
    QIcon::ThemeIcon icon,
    const QIcon *fallback) {
  return new QIcon(QIcon::fromTheme(icon, *fallback));
}

//  bool QIcon::hasThemeIcon(ThemeIcon icon)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QIcon12hasThemeIconENS_9ThemeIconE(QIcon::ThemeIcon icon) {
  return QIcon::hasThemeIcon(icon);
}

//  QStringList QIcon::themeSearchPaths()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN5QIcon16themeSearchPathsEv() {
  return new QList<QString>(QIcon::themeSearchPaths());
}

//  void QIcon::setThemeSearchPaths(const QStringList &searchpath)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QIcon19setThemeSearchPathsERK5QListI7QStringE(
    const QList<QString> *searchpath) {
  QIcon::setThemeSearchPaths(*searchpath);
}

//  QStringList QIcon::fallbackSearchPaths()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN5QIcon19fallbackSearchPathsEv() {
  return new QList<QString>(QIcon::fallbackSearchPaths());
}

//  void QIcon::setFallbackSearchPaths(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QIcon22setFallbackSearchPathsERK5QListI7QStringE(
    const QList<QString> *paths) {
  QIcon::setFallbackSearchPaths(*paths);
}

//  QString QIcon::themeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QIcon9themeNameEv() {
  return new QString(QIcon::themeName());
}

//  void QIcon::setThemeName(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QIcon12setThemeNameERK7QString(const QString *path) {
  QIcon::setThemeName(*path);
}

//  QString QIcon::fallbackThemeName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QIcon17fallbackThemeNameEv() {
  return new QString(QIcon::fallbackThemeName());
}

//  void QIcon::setFallbackThemeName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QIcon20setFallbackThemeNameERK7QString(const QString *name) {
  QIcon::setFallbackThemeName(*name);
}
