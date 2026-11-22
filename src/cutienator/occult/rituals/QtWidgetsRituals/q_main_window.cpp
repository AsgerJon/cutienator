//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmainwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmainwindow.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QMainWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QMainWindow10metaObjectEv(
    const QMainWindow *self) {
  return self->metaObject();
}

//  QString QMainWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QMainWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMainWindow::tr(s, c, n));
}

//  QMainWindow::QMainWindow(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QMainWindow *ritual_ZN11QMainWindowC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new QMainWindow(parent, QFlags<Qt::WindowType>::fromInt(flags));
}

//  QMainWindow::~QMainWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindowD1Ev(QMainWindow *self) {
  delete self;
}

//  QSize QMainWindow::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QMainWindow8iconSizeEv(const QMainWindow *self) {
  return new QSize(self->iconSize());
}

//  void QMainWindow::setIconSize(const QSize &iconSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow11setIconSizeERK5QSize(
    QMainWindow *self,
    const QSize *iconSize) {
  self->setIconSize(*iconSize);
}

//  Qt::ToolButtonStyle QMainWindow::toolButtonStyle() const
extern "C" Q_DECL_EXPORT
Qt::ToolButtonStyle ritual_ZNK11QMainWindow15toolButtonStyleEv(
    const QMainWindow *self) {
  return self->toolButtonStyle();
}

//  void QMainWindow::setToolButtonStyle(Qt::ToolButtonStyle toolButtonStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow18setToolButtonStyleEN2Qt15ToolButtonStyleE(
    QMainWindow *self,
    Qt::ToolButtonStyle toolButtonStyle) {
  self->setToolButtonStyle(toolButtonStyle);
}

//  bool QMainWindow::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow10isAnimatedEv(const QMainWindow *self) {
  return self->isAnimated();
}

//  bool QMainWindow::isDockNestingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow20isDockNestingEnabledEv(
    const QMainWindow *self) {
  return self->isDockNestingEnabled();
}

//  bool QMainWindow::documentMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow12documentModeEv(const QMainWindow *self) {
  return self->documentMode();
}

//  void QMainWindow::setDocumentMode(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow15setDocumentModeEb(
    QMainWindow *self,
    bool enabled) {
  self->setDocumentMode(enabled);
}

//  QTabWidget::TabShape QMainWindow::tabShape() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabShape ritual_ZNK11QMainWindow8tabShapeEv(
    const QMainWindow *self) {
  return self->tabShape();
}

//  void QMainWindow::setTabShape(QTabWidget::TabShape tabShape)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow11setTabShapeEN10QTabWidget8TabShapeE(
    QMainWindow *self,
    QTabWidget::TabShape tabShape) {
  self->setTabShape(tabShape);
}

//  QTabWidget::TabPosition QMainWindow::tabPosition(Qt::DockWidgetArea area)
//      const
extern "C" Q_DECL_EXPORT
QTabWidget::TabPosition ritual_ZNK11QMainWindow11tabPositionEN2Qt14DockWidgetAreaE(
    const QMainWindow *self,
    Qt::DockWidgetArea area) {
  return self->tabPosition(area);
}

//  void QMainWindow::setTabPosition(Qt::DockWidgetAreas areas,
//      QTabWidget::TabPosition tabPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow14setTabPositionE6QFlagsIN2Qt14DockWidgetAreaEEN10QTabWidget11TabPositionE(
    QMainWindow *self,
    int areas,
    QTabWidget::TabPosition tabPosition) {
  self->setTabPosition(
      QFlags<Qt::DockWidgetArea>::fromInt(areas),
      tabPosition);
}

//  void QMainWindow::setDockOptions(DockOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow14setDockOptionsE6QFlagsINS_10DockOptionEE(
    QMainWindow *self,
    int options) {
  self->setDockOptions(QFlags<QMainWindow::DockOption>::fromInt(options));
}

//  DockOptions QMainWindow::dockOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMainWindow11dockOptionsEv(const QMainWindow *self) {
  return static_cast<int>(self->dockOptions().toInt());
}

//  bool QMainWindow::isSeparator(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow11isSeparatorERK6QPoint(
    const QMainWindow *self,
    const QPoint *pos) {
  return self->isSeparator(*pos);
}

//  QMenuBar *QMainWindow::menuBar() const
extern "C" Q_DECL_EXPORT
QMenuBar *ritual_ZNK11QMainWindow7menuBarEv(const QMainWindow *self) {
  return self->menuBar();
}

//  void QMainWindow::setMenuBar(QMenuBar *menubar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow10setMenuBarEP8QMenuBar(
    QMainWindow *self,
    QMenuBar *menubar) {
  self->setMenuBar(menubar);
}

//  QWidget *QMainWindow::menuWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QMainWindow10menuWidgetEv(const QMainWindow *self) {
  return self->menuWidget();
}

//  void QMainWindow::setMenuWidget(QWidget *menubar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow13setMenuWidgetEP7QWidget(
    QMainWindow *self,
    QWidget *menubar) {
  self->setMenuWidget(menubar);
}

//  QStatusBar *QMainWindow::statusBar() const
extern "C" Q_DECL_EXPORT
QStatusBar *ritual_ZNK11QMainWindow9statusBarEv(const QMainWindow *self) {
  return self->statusBar();
}

//  void QMainWindow::setStatusBar(QStatusBar *statusbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow12setStatusBarEP10QStatusBar(
    QMainWindow *self,
    QStatusBar *statusbar) {
  self->setStatusBar(statusbar);
}

//  QWidget *QMainWindow::centralWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QMainWindow13centralWidgetEv(const QMainWindow *self) {
  return self->centralWidget();
}

//  void QMainWindow::setCentralWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow16setCentralWidgetEP7QWidget(
    QMainWindow *self,
    QWidget *widget) {
  self->setCentralWidget(widget);
}

//  QWidget *QMainWindow::takeCentralWidget()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN11QMainWindow17takeCentralWidgetEv(QMainWindow *self) {
  return self->takeCentralWidget();
}

//  void QMainWindow::setCorner(Qt::Corner corner, Qt::DockWidgetArea area)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow9setCornerEN2Qt6CornerENS0_14DockWidgetAreaE(
    QMainWindow *self,
    Qt::Corner corner,
    Qt::DockWidgetArea area) {
  self->setCorner(corner, area);
}

//  Qt::DockWidgetArea QMainWindow::corner(Qt::Corner corner) const
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZNK11QMainWindow6cornerEN2Qt6CornerE(
    const QMainWindow *self,
    Qt::Corner corner) {
  return self->corner(corner);
}

//  void QMainWindow::addToolBarBreak(Qt::ToolBarArea area)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow15addToolBarBreakEN2Qt11ToolBarAreaE(
    QMainWindow *self,
    Qt::ToolBarArea area) {
  self->addToolBarBreak(area);
}

//  void QMainWindow::insertToolBarBreak(QToolBar *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow18insertToolBarBreakEP8QToolBar(
    QMainWindow *self,
    QToolBar *before) {
  self->insertToolBarBreak(before);
}

//  void QMainWindow::addToolBar(Qt::ToolBarArea area, QToolBar *toolbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow10addToolBarEN2Qt11ToolBarAreaEP8QToolBar(
    QMainWindow *self,
    Qt::ToolBarArea area,
    QToolBar *toolbar) {
  self->addToolBar(area, toolbar);
}

//  void QMainWindow::addToolBar(QToolBar *toolbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow10addToolBarEP8QToolBar(
    QMainWindow *self,
    QToolBar *toolbar) {
  self->addToolBar(toolbar);
}

//  QToolBar *QMainWindow::addToolBar(const QString &title)
extern "C" Q_DECL_EXPORT
QToolBar *ritual_ZN11QMainWindow10addToolBarERK7QString(
    QMainWindow *self,
    const QString *title) {
  return self->addToolBar(*title);
}

//  void QMainWindow::insertToolBar(QToolBar *before, QToolBar *toolbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow13insertToolBarEP8QToolBarS1_(
    QMainWindow *self,
    QToolBar *before,
    QToolBar *toolbar) {
  self->insertToolBar(before, toolbar);
}

//  void QMainWindow::removeToolBar(QToolBar *toolbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow13removeToolBarEP8QToolBar(
    QMainWindow *self,
    QToolBar *toolbar) {
  self->removeToolBar(toolbar);
}

//  void QMainWindow::removeToolBarBreak(QToolBar *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow18removeToolBarBreakEP8QToolBar(
    QMainWindow *self,
    QToolBar *before) {
  self->removeToolBarBreak(before);
}

//  bool QMainWindow::unifiedTitleAndToolBarOnMac() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow27unifiedTitleAndToolBarOnMacEv(
    const QMainWindow *self) {
  return self->unifiedTitleAndToolBarOnMac();
}

//  Qt::ToolBarArea QMainWindow::toolBarArea(const QToolBar *toolbar) const
extern "C" Q_DECL_EXPORT
Qt::ToolBarArea ritual_ZNK11QMainWindow11toolBarAreaEPK8QToolBar(
    const QMainWindow *self,
    const QToolBar *toolbar) {
  return self->toolBarArea(toolbar);
}

//  bool QMainWindow::toolBarBreak(QToolBar *toolbar) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMainWindow12toolBarBreakEP8QToolBar(
    const QMainWindow *self,
    QToolBar *toolbar) {
  return self->toolBarBreak(toolbar);
}

//  void QMainWindow::addDockWidget(Qt::DockWidgetArea area, QDockWidget
//      *dockwidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow13addDockWidgetEN2Qt14DockWidgetAreaEP11QDockWidget(
    QMainWindow *self,
    Qt::DockWidgetArea area,
    QDockWidget *dockwidget) {
  self->addDockWidget(area, dockwidget);
}

//  void QMainWindow::addDockWidget(Qt::DockWidgetArea area, QDockWidget
//      *dockwidget, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow13addDockWidgetEN2Qt14DockWidgetAreaEP11QDockWidgetNS0_11OrientationE(
    QMainWindow *self,
    Qt::DockWidgetArea area,
    QDockWidget *dockwidget,
    Qt::Orientation orientation) {
  self->addDockWidget(area, dockwidget, orientation);
}

//  void QMainWindow::splitDockWidget(QDockWidget *after, QDockWidget
//      *dockwidget, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow15splitDockWidgetEP11QDockWidgetS1_N2Qt11OrientationE(
    QMainWindow *self,
    QDockWidget *after,
    QDockWidget *dockwidget,
    Qt::Orientation orientation) {
  self->splitDockWidget(after, dockwidget, orientation);
}

//  void QMainWindow::tabifyDockWidget(QDockWidget *first, QDockWidget
//      *second)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow16tabifyDockWidgetEP11QDockWidgetS1_(
    QMainWindow *self,
    QDockWidget *first,
    QDockWidget *second) {
  self->tabifyDockWidget(first, second);
}

//  void QMainWindow::removeDockWidget(QDockWidget *dockwidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow16removeDockWidgetEP11QDockWidget(
    QMainWindow *self,
    QDockWidget *dockwidget) {
  self->removeDockWidget(dockwidget);
}

//  bool QMainWindow::restoreDockWidget(QDockWidget *dockwidget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMainWindow17restoreDockWidgetEP11QDockWidget(
    QMainWindow *self,
    QDockWidget *dockwidget) {
  return self->restoreDockWidget(dockwidget);
}

//  Qt::DockWidgetArea QMainWindow::dockWidgetArea(QDockWidget *dockwidget)
//      const
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZNK11QMainWindow14dockWidgetAreaEP11QDockWidget(
    const QMainWindow *self,
    QDockWidget *dockwidget) {
  return self->dockWidgetArea(dockwidget);
}

//  QByteArray QMainWindow::saveState(int version) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QMainWindow9saveStateEi(
    const QMainWindow *self,
    int version) {
  return new QByteArray(self->saveState(version));
}

//  bool QMainWindow::restoreState(const QByteArray &state, int version)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMainWindow12restoreStateERK10QByteArrayi(
    QMainWindow *self,
    const QByteArray *state,
    int version) {
  return self->restoreState(*state, version);
}

//  QMenu *QMainWindow::createPopupMenu()
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN11QMainWindow15createPopupMenuEv(QMainWindow *self) {
  return self->createPopupMenu();
}

//  void QMainWindow::setAnimated(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow11setAnimatedEb(QMainWindow *self, bool enabled) {
  self->setAnimated(enabled);
}

//  void QMainWindow::setDockNestingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow21setDockNestingEnabledEb(
    QMainWindow *self,
    bool enabled) {
  self->setDockNestingEnabled(enabled);
}

//  void QMainWindow::setUnifiedTitleAndToolBarOnMac(bool set)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMainWindow30setUnifiedTitleAndToolBarOnMacEb(
    QMainWindow *self,
    bool set) {
  self->setUnifiedTitleAndToolBarOnMac(set);
}
