//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qwindow.h>
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtGui/qregion.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qpoint.h>
#include <QtGui/qicon.h>
#include <QtGui/qcursor.h>

//  const QMetaObject *QWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QWindow10metaObjectEv(const QWindow *self) {
  return self->metaObject();
}

//  QString QWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QWindow2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QWindow::tr(s, c, n));
}

//  QWindow::QWindow(QScreen *screen)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN7QWindowC1EP7QScreen(QScreen *screen) {
  return new QWindow(screen);
}

//  QWindow::QWindow(QWindow *parent)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN7QWindowC1EPS_(QWindow *parent) {
  return new QWindow(parent);
}

//  QWindow::~QWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindowD1Ev(QWindow *self) {
  delete self;
}

//  void QWindow::setSurfaceType(SurfaceType surfaceType)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14setSurfaceTypeEN8QSurface11SurfaceTypeE(
    QWindow *self,
    QSurface::SurfaceType surfaceType) {
  self->setSurfaceType(surfaceType);
}

//  SurfaceType QWindow::surfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZNK7QWindow11surfaceTypeEv(
    const QWindow *self) {
  return self->surfaceType();
}

//  bool QWindow::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow9isVisibleEv(const QWindow *self) {
  return self->isVisible();
}

//  Visibility QWindow::visibility() const
extern "C" Q_DECL_EXPORT
QWindow::Visibility ritual_ZNK7QWindow10visibilityEv(const QWindow *self) {
  return self->visibility();
}

//  void QWindow::setVisibility(Visibility v)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow13setVisibilityENS_10VisibilityE(
    QWindow *self,
    QWindow::Visibility v) {
  self->setVisibility(v);
}

//  void QWindow::create()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow6createEv(QWindow *self) {
  self->create();
}

//  WId QWindow::winId() const
extern "C" Q_DECL_EXPORT
WId ritual_ZNK7QWindow5winIdEv(const QWindow *self) {
  return self->winId();
}

//  QWindow *QWindow::parent(AncestorMode mode) const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK7QWindow6parentENS_12AncestorModeE(
    const QWindow *self,
    QWindow::AncestorMode mode) {
  return self->parent(mode);
}

//  void QWindow::setParent(QWindow *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9setParentEPS_(QWindow *self, QWindow *parent) {
  self->setParent(parent);
}

//  bool QWindow::isTopLevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow10isTopLevelEv(const QWindow *self) {
  return self->isTopLevel();
}

//  bool QWindow::isModal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow7isModalEv(const QWindow *self) {
  return self->isModal();
}

//  Qt::WindowModality QWindow::modality() const
extern "C" Q_DECL_EXPORT
Qt::WindowModality ritual_ZNK7QWindow8modalityEv(const QWindow *self) {
  return self->modality();
}

//  void QWindow::setModality(Qt::WindowModality modality)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setModalityEN2Qt14WindowModalityE(
    QWindow *self,
    Qt::WindowModality modality) {
  self->setModality(modality);
}

//  void QWindow::setFormat(const QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9setFormatERK14QSurfaceFormat(
    QWindow *self,
    const QSurfaceFormat *format) {
  self->setFormat(*format);
}

//  QSurfaceFormat QWindow::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK7QWindow6formatEv(const QWindow *self) {
  return new QSurfaceFormat(self->format());
}

//  QSurfaceFormat QWindow::requestedFormat() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK7QWindow15requestedFormatEv(const QWindow *self) {
  return new QSurfaceFormat(self->requestedFormat());
}

//  void QWindow::setFlags(Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow8setFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QWindow *self,
    int flags) {
  self->setFlags(QFlags<Qt::WindowType>::fromInt(flags));
}

//  Qt::WindowFlags QWindow::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow5flagsEv(const QWindow *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QWindow::setFlag(Qt::WindowType a0, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow7setFlagEN2Qt10WindowTypeEb(
    QWindow *self,
    Qt::WindowType a0,
    bool on) {
  self->setFlag(a0, on);
}

//  Qt::WindowType QWindow::type() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_ZNK7QWindow4typeEv(const QWindow *self) {
  return self->type();
}

//  QString QWindow::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWindow5titleEv(const QWindow *self) {
  return new QString(self->title());
}

//  void QWindow::setOpacity(qreal level)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow10setOpacityEd(QWindow *self, qreal level) {
  self->setOpacity(level);
}

//  qreal QWindow::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QWindow7opacityEv(const QWindow *self) {
  return self->opacity();
}

//  void QWindow::setMask(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow7setMaskERK7QRegion(
    QWindow *self,
    const QRegion *region) {
  self->setMask(*region);
}

//  QRegion QWindow::mask() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QWindow4maskEv(const QWindow *self) {
  return new QRegion(self->mask());
}

//  bool QWindow::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow8isActiveEv(const QWindow *self) {
  return self->isActive();
}

//  void QWindow::reportContentOrientationChange(Qt::ScreenOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow30reportContentOrientationChangeEN2Qt17ScreenOrientationE(
    QWindow *self,
    Qt::ScreenOrientation orientation) {
  self->reportContentOrientationChange(orientation);
}

//  Qt::ScreenOrientation QWindow::contentOrientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK7QWindow18contentOrientationEv(
    const QWindow *self) {
  return self->contentOrientation();
}

//  qreal QWindow::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QWindow16devicePixelRatioEv(const QWindow *self) {
  return self->devicePixelRatio();
}

//  Qt::WindowState QWindow::windowState() const
extern "C" Q_DECL_EXPORT
Qt::WindowState ritual_ZNK7QWindow11windowStateEv(const QWindow *self) {
  return self->windowState();
}

//  Qt::WindowStates QWindow::windowStates() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow12windowStatesEv(const QWindow *self) {
  return static_cast<int>(self->windowStates().toInt());
}

//  void QWindow::setWindowState(Qt::WindowState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14setWindowStateEN2Qt11WindowStateE(
    QWindow *self,
    Qt::WindowState state) {
  self->setWindowState(state);
}

//  void QWindow::setWindowStates(Qt::WindowStates states)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow15setWindowStatesE6QFlagsIN2Qt11WindowStateEE(
    QWindow *self,
    int states) {
  self->setWindowStates(QFlags<Qt::WindowState>::fromInt(states));
}

//  void QWindow::setTransientParent(QWindow *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow18setTransientParentEPS_(
    QWindow *self,
    QWindow *parent) {
  self->setTransientParent(parent);
}

//  QWindow *QWindow::transientParent() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK7QWindow15transientParentEv(const QWindow *self) {
  return self->transientParent();
}

//  bool QWindow::isAncestorOf(const QWindow *child, AncestorMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow12isAncestorOfEPKS_NS_12AncestorModeE(
    const QWindow *self,
    const QWindow *child,
    QWindow::AncestorMode mode) {
  return self->isAncestorOf(child, mode);
}

//  bool QWindow::isExposed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow9isExposedEv(const QWindow *self) {
  return self->isExposed();
}

//  int QWindow::minimumWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow12minimumWidthEv(const QWindow *self) {
  return self->minimumWidth();
}

//  int QWindow::minimumHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow13minimumHeightEv(const QWindow *self) {
  return self->minimumHeight();
}

//  int QWindow::maximumWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow12maximumWidthEv(const QWindow *self) {
  return self->maximumWidth();
}

//  int QWindow::maximumHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow13maximumHeightEv(const QWindow *self) {
  return self->maximumHeight();
}

//  QSize QWindow::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWindow11minimumSizeEv(const QWindow *self) {
  return new QSize(self->minimumSize());
}

//  QSize QWindow::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWindow11maximumSizeEv(const QWindow *self) {
  return new QSize(self->maximumSize());
}

//  QSize QWindow::baseSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWindow8baseSizeEv(const QWindow *self) {
  return new QSize(self->baseSize());
}

//  QSize QWindow::sizeIncrement() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWindow13sizeIncrementEv(const QWindow *self) {
  return new QSize(self->sizeIncrement());
}

//  void QWindow::setMinimumSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14setMinimumSizeERK5QSize(
    QWindow *self,
    const QSize *size) {
  self->setMinimumSize(*size);
}

//  void QWindow::setMaximumSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14setMaximumSizeERK5QSize(
    QWindow *self,
    const QSize *size) {
  self->setMaximumSize(*size);
}

//  void QWindow::setBaseSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setBaseSizeERK5QSize(
    QWindow *self,
    const QSize *size) {
  self->setBaseSize(*size);
}

//  void QWindow::setSizeIncrement(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow16setSizeIncrementERK5QSize(
    QWindow *self,
    const QSize *size) {
  self->setSizeIncrement(*size);
}

//  QRect QWindow::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QWindow8geometryEv(const QWindow *self) {
  return new QRect(self->geometry());
}

//  QMargins QWindow::frameMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK7QWindow12frameMarginsEv(const QWindow *self) {
  return new QMargins(self->frameMargins());
}

//  QRect QWindow::frameGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QWindow13frameGeometryEv(const QWindow *self) {
  return new QRect(self->frameGeometry());
}

//  QPoint QWindow::framePosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWindow13framePositionEv(const QWindow *self) {
  return new QPoint(self->framePosition());
}

//  void QWindow::setFramePosition(const QPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow16setFramePositionERK6QPoint(
    QWindow *self,
    const QPoint *point) {
  self->setFramePosition(*point);
}

//  void QWindow::setFramePosition(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow16setFramePositionEii(QWindow *self, int x, int y) {
  self->setFramePosition(x, y);
}

//  QMargins QWindow::safeAreaMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK7QWindow15safeAreaMarginsEv(const QWindow *self) {
  return new QMargins(self->safeAreaMargins());
}

//  int QWindow::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow5widthEv(const QWindow *self) {
  return self->width();
}

//  int QWindow::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow6heightEv(const QWindow *self) {
  return self->height();
}

//  int QWindow::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow1xEv(const QWindow *self) {
  return self->x();
}

//  int QWindow::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow1yEv(const QWindow *self) {
  return self->y();
}

//  QSize QWindow::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWindow4sizeEv(const QWindow *self) {
  return new QSize(self->size());
}

//  QPoint QWindow::position() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWindow8positionEv(const QWindow *self) {
  return new QPoint(self->position());
}

//  void QWindow::setPosition(const QPoint &pt)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setPositionERK6QPoint(
    QWindow *self,
    const QPoint *pt) {
  self->setPosition(*pt);
}

//  void QWindow::setPosition(int posx, int posy)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setPositionEii(QWindow *self, int posx, int posy) {
  self->setPosition(posx, posy);
}

//  void QWindow::resize(const QSize &newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow6resizeERK5QSize(QWindow *self, const QSize *newSize) {
  self->resize(*newSize);
}

//  void QWindow::resize(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow6resizeEii(QWindow *self, int w, int h) {
  self->resize(w, h);
}

//  void QWindow::setFilePath(const QString &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setFilePathERK7QString(
    QWindow *self,
    const QString *filePath) {
  self->setFilePath(*filePath);
}

//  QString QWindow::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWindow8filePathEv(const QWindow *self) {
  return new QString(self->filePath());
}

//  void QWindow::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow7setIconERK5QIcon(QWindow *self, const QIcon *icon) {
  self->setIcon(*icon);
}

//  QIcon QWindow::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK7QWindow4iconEv(const QWindow *self) {
  return new QIcon(self->icon());
}

//  void QWindow::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow7destroyEv(QWindow *self) {
  self->destroy();
}

//  bool QWindow::setKeyboardGrabEnabled(bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow22setKeyboardGrabEnabledEb(QWindow *self, bool grab) {
  return self->setKeyboardGrabEnabled(grab);
}

//  bool QWindow::setMouseGrabEnabled(bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow19setMouseGrabEnabledEb(QWindow *self, bool grab) {
  return self->setMouseGrabEnabled(grab);
}

//  QScreen *QWindow::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK7QWindow6screenEv(const QWindow *self) {
  return self->screen();
}

//  void QWindow::setScreen(QScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9setScreenEP7QScreen(QWindow *self, QScreen *screen) {
  self->setScreen(screen);
}

//  QAccessibleInterface *QWindow::accessibleRoot() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK7QWindow14accessibleRootEv(
    const QWindow *self) {
  return self->accessibleRoot();
}

//  QObject *QWindow::focusObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK7QWindow11focusObjectEv(const QWindow *self) {
  return self->focusObject();
}

//  QPointF QWindow::mapToGlobal(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QWindow11mapToGlobalERK7QPointF(
    const QWindow *self,
    const QPointF *pos) {
  return new QPointF(self->mapToGlobal(*pos));
}

//  QPointF QWindow::mapFromGlobal(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QWindow13mapFromGlobalERK7QPointF(
    const QWindow *self,
    const QPointF *pos) {
  return new QPointF(self->mapFromGlobal(*pos));
}

//  QPoint QWindow::mapToGlobal(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWindow11mapToGlobalERK6QPoint(
    const QWindow *self,
    const QPoint *pos) {
  return new QPoint(self->mapToGlobal(*pos));
}

//  QPoint QWindow::mapFromGlobal(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWindow13mapFromGlobalERK6QPoint(
    const QWindow *self,
    const QPoint *pos) {
  return new QPoint(self->mapFromGlobal(*pos));
}

//  QCursor QWindow::cursor() const
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZNK7QWindow6cursorEv(const QWindow *self) {
  return new QCursor(self->cursor());
}

//  void QWindow::setCursor(const QCursor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9setCursorERK7QCursor(
    QWindow *self,
    const QCursor *a0) {
  self->setCursor(*a0);
}

//  void QWindow::unsetCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11unsetCursorEv(QWindow *self) {
  self->unsetCursor();
}

//  QWindow *QWindow::fromWinId(WId id)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN7QWindow9fromWinIdEy(WId id) {
  return QWindow::fromWinId(id);
}

//  void QWindow::requestActivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow15requestActivateEv(QWindow *self) {
  self->requestActivate();
}

//  void QWindow::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow10setVisibleEb(QWindow *self, bool visible) {
  self->setVisible(visible);
}

//  void QWindow::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow4showEv(QWindow *self) {
  self->show();
}

//  void QWindow::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow4hideEv(QWindow *self) {
  self->hide();
}

//  void QWindow::showMinimized()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow13showMinimizedEv(QWindow *self) {
  self->showMinimized();
}

//  void QWindow::showMaximized()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow13showMaximizedEv(QWindow *self) {
  self->showMaximized();
}

//  void QWindow::showFullScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14showFullScreenEv(QWindow *self) {
  self->showFullScreen();
}

//  void QWindow::showNormal()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow10showNormalEv(QWindow *self) {
  self->showNormal();
}

//  bool QWindow::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow5closeEv(QWindow *self) {
  return self->close();
}

//  void QWindow::raise()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow5raiseEv(QWindow *self) {
  self->raise();
}

//  void QWindow::lower()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow5lowerEv(QWindow *self) {
  self->lower();
}

//  bool QWindow::startSystemResize(Qt::Edges edges)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow17startSystemResizeE6QFlagsIN2Qt4EdgeEE(
    QWindow *self,
    int edges) {
  return self->startSystemResize(QFlags<Qt::Edge>::fromInt(edges));
}

//  bool QWindow::startSystemMove()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow15startSystemMoveEv(QWindow *self) {
  return self->startSystemMove();
}

//  void QWindow::setTitle(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow8setTitleERK7QString(
    QWindow *self,
    const QString *a0) {
  self->setTitle(*a0);
}

//  void QWindow::setX(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow4setXEi(QWindow *self, int arg) {
  self->setX(arg);
}

//  void QWindow::setY(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow4setYEi(QWindow *self, int arg) {
  self->setY(arg);
}

//  void QWindow::setWidth(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow8setWidthEi(QWindow *self, int arg) {
  self->setWidth(arg);
}

//  void QWindow::setHeight(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9setHeightEi(QWindow *self, int arg) {
  self->setHeight(arg);
}

//  void QWindow::setGeometry(int posx, int posy, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setGeometryEiiii(
    QWindow *self,
    int posx,
    int posy,
    int w,
    int h) {
  self->setGeometry(posx, posy, w, h);
}

//  void QWindow::setGeometry(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setGeometryERK5QRect(
    QWindow *self,
    const QRect *rect) {
  self->setGeometry(*rect);
}

//  void QWindow::setMinimumWidth(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow15setMinimumWidthEi(QWindow *self, int w) {
  self->setMinimumWidth(w);
}

//  void QWindow::setMinimumHeight(int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow16setMinimumHeightEi(QWindow *self, int h) {
  self->setMinimumHeight(h);
}

//  void QWindow::setMaximumWidth(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow15setMaximumWidthEi(QWindow *self, int w) {
  self->setMaximumWidth(w);
}

//  void QWindow::setMaximumHeight(int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow16setMaximumHeightEi(QWindow *self, int h) {
  self->setMaximumHeight(h);
}

//  void QWindow::alert(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow5alertEi(QWindow *self, int msec) {
  self->alert(msec);
}

//  void QWindow::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow13requestUpdateEv(QWindow *self) {
  self->requestUpdate();
}
