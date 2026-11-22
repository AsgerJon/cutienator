//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtoolbar.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtoolbar.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QToolBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QToolBar10metaObjectEv(const QToolBar *self) {
  return self->metaObject();
}

//  QString QToolBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QToolBar2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QToolBar::tr(s, c, n));
}

//  QToolBar::QToolBar(const QString &title, QWidget *parent)
extern "C" Q_DECL_EXPORT
QToolBar *ritual_ZN8QToolBarC1ERK7QStringP7QWidget(
    const QString *title,
    QWidget *parent) {
  return new QToolBar(*title, parent);
}

//  QToolBar::QToolBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QToolBar *ritual_ZN8QToolBarC1EP7QWidget(QWidget *parent) {
  return new QToolBar(parent);
}

//  QToolBar::~QToolBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBarD1Ev(QToolBar *self) {
  delete self;
}

//  void QToolBar::setMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar10setMovableEb(QToolBar *self, bool movable) {
  self->setMovable(movable);
}

//  bool QToolBar::isMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QToolBar9isMovableEv(const QToolBar *self) {
  return self->isMovable();
}

//  void QToolBar::setAllowedAreas(Qt::ToolBarAreas areas)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar15setAllowedAreasE6QFlagsIN2Qt11ToolBarAreaEE(
    QToolBar *self,
    int areas) {
  self->setAllowedAreas(QFlags<Qt::ToolBarArea>::fromInt(areas));
}

//  Qt::ToolBarAreas QToolBar::allowedAreas() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QToolBar12allowedAreasEv(const QToolBar *self) {
  return static_cast<int>(self->allowedAreas().toInt());
}

//  bool QToolBar::isAreaAllowed(Qt::ToolBarArea area) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QToolBar13isAreaAllowedEN2Qt11ToolBarAreaE(
    const QToolBar *self,
    Qt::ToolBarArea area) {
  return self->isAreaAllowed(area);
}

//  void QToolBar::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar14setOrientationEN2Qt11OrientationE(
    QToolBar *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  Qt::Orientation QToolBar::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK8QToolBar11orientationEv(const QToolBar *self) {
  return self->orientation();
}

//  void QToolBar::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar5clearEv(QToolBar *self) {
  self->clear();
}

//  QAction *QToolBar::addSeparator()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QToolBar12addSeparatorEv(QToolBar *self) {
  return self->addSeparator();
}

//  QAction *QToolBar::insertSeparator(QAction *before)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QToolBar15insertSeparatorEP7QAction(
    QToolBar *self,
    QAction *before) {
  return self->insertSeparator(before);
}

//  QAction *QToolBar::addWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QToolBar9addWidgetEP7QWidget(
    QToolBar *self,
    QWidget *widget) {
  return self->addWidget(widget);
}

//  QAction *QToolBar::insertWidget(QAction *before, QWidget *widget)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QToolBar12insertWidgetEP7QActionP7QWidget(
    QToolBar *self,
    QAction *before,
    QWidget *widget) {
  return self->insertWidget(before, widget);
}

//  QRect QToolBar::actionGeometry(QAction *action) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8QToolBar14actionGeometryEP7QAction(
    const QToolBar *self,
    QAction *action) {
  return new QRect(self->actionGeometry(action));
}

//  QAction *QToolBar::actionAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK8QToolBar8actionAtERK6QPoint(
    const QToolBar *self,
    const QPoint *p) {
  return self->actionAt(*p);
}

//  QAction *QToolBar::actionAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK8QToolBar8actionAtEii(
    const QToolBar *self,
    int x,
    int y) {
  return self->actionAt(x, y);
}

//  QAction *QToolBar::toggleViewAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK8QToolBar16toggleViewActionEv(const QToolBar *self) {
  return self->toggleViewAction();
}

//  QSize QToolBar::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QToolBar8iconSizeEv(const QToolBar *self) {
  return new QSize(self->iconSize());
}

//  Qt::ToolButtonStyle QToolBar::toolButtonStyle() const
extern "C" Q_DECL_EXPORT
Qt::ToolButtonStyle ritual_ZNK8QToolBar15toolButtonStyleEv(
    const QToolBar *self) {
  return self->toolButtonStyle();
}

//  QWidget *QToolBar::widgetForAction(QAction *action) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK8QToolBar15widgetForActionEP7QAction(
    const QToolBar *self,
    QAction *action) {
  return self->widgetForAction(action);
}

//  bool QToolBar::isFloatable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QToolBar11isFloatableEv(const QToolBar *self) {
  return self->isFloatable();
}

//  void QToolBar::setFloatable(bool floatable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar12setFloatableEb(QToolBar *self, bool floatable) {
  self->setFloatable(floatable);
}

//  bool QToolBar::isFloating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QToolBar10isFloatingEv(const QToolBar *self) {
  return self->isFloating();
}

//  void QToolBar::setIconSize(const QSize &iconSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar11setIconSizeERK5QSize(
    QToolBar *self,
    const QSize *iconSize) {
  self->setIconSize(*iconSize);
}

//  void QToolBar::setToolButtonStyle(Qt::ToolButtonStyle toolButtonStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QToolBar18setToolButtonStyleEN2Qt15ToolButtonStyleE(
    QToolBar *self,
    Qt::ToolButtonStyle toolButtonStyle) {
  self->setToolButtonStyle(toolButtonStyle);
}
