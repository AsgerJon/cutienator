//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmenubar.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmenubar.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QMenuBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QMenuBar10metaObjectEv(const QMenuBar *self) {
  return self->metaObject();
}

//  QString QMenuBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QMenuBar2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QMenuBar::tr(s, c, n));
}

//  QMenuBar::QMenuBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QMenuBar *ritual_ZN8QMenuBarC1EP7QWidget(QWidget *parent) {
  return new QMenuBar(parent);
}

//  QMenuBar::~QMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBarD1Ev(QMenuBar *self) {
  delete self;
}

//  QAction *QMenuBar::addMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QMenuBar7addMenuEP5QMenu(QMenuBar *self, QMenu *menu) {
  return self->addMenu(menu);
}

//  QMenu *QMenuBar::addMenu(const QString &title)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN8QMenuBar7addMenuERK7QString(
    QMenuBar *self,
    const QString *title) {
  return self->addMenu(*title);
}

//  QMenu *QMenuBar::addMenu(const QIcon &icon, const QString &title)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN8QMenuBar7addMenuERK5QIconRK7QString(
    QMenuBar *self,
    const QIcon *icon,
    const QString *title) {
  return self->addMenu(*icon, *title);
}

//  QAction *QMenuBar::addSeparator()
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QMenuBar12addSeparatorEv(QMenuBar *self) {
  return self->addSeparator();
}

//  QAction *QMenuBar::insertSeparator(QAction *before)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QMenuBar15insertSeparatorEP7QAction(
    QMenuBar *self,
    QAction *before) {
  return self->insertSeparator(before);
}

//  QAction *QMenuBar::insertMenu(QAction *before, QMenu *menu)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN8QMenuBar10insertMenuEP7QActionP5QMenu(
    QMenuBar *self,
    QAction *before,
    QMenu *menu) {
  return self->insertMenu(before, menu);
}

//  void QMenuBar::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar5clearEv(QMenuBar *self) {
  self->clear();
}

//  QAction *QMenuBar::activeAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK8QMenuBar12activeActionEv(const QMenuBar *self) {
  return self->activeAction();
}

//  void QMenuBar::setActiveAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar15setActiveActionEP7QAction(
    QMenuBar *self,
    QAction *action) {
  self->setActiveAction(action);
}

//  void QMenuBar::setDefaultUp(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar12setDefaultUpEb(QMenuBar *self, bool a0) {
  self->setDefaultUp(a0);
}

//  bool QMenuBar::isDefaultUp() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMenuBar11isDefaultUpEv(const QMenuBar *self) {
  return self->isDefaultUp();
}

//  QSize QMenuBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QMenuBar8sizeHintEv(const QMenuBar *self) {
  return new QSize(self->sizeHint());
}

//  QSize QMenuBar::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QMenuBar15minimumSizeHintEv(const QMenuBar *self) {
  return new QSize(self->minimumSizeHint());
}

//  int QMenuBar::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QMenuBar14heightForWidthEi(const QMenuBar *self, int a0) {
  return self->heightForWidth(a0);
}

//  QRect QMenuBar::actionGeometry(QAction *a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8QMenuBar14actionGeometryEP7QAction(
    const QMenuBar *self,
    QAction *a0) {
  return new QRect(self->actionGeometry(a0));
}

//  QAction *QMenuBar::actionAt(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK8QMenuBar8actionAtERK6QPoint(
    const QMenuBar *self,
    const QPoint *a0) {
  return self->actionAt(*a0);
}

//  void QMenuBar::setCornerWidget(QWidget *w, Qt::Corner corner)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar15setCornerWidgetEP7QWidgetN2Qt6CornerE(
    QMenuBar *self,
    QWidget *w,
    Qt::Corner corner) {
  self->setCornerWidget(w, corner);
}

//  QWidget *QMenuBar::cornerWidget(Qt::Corner corner) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK8QMenuBar12cornerWidgetEN2Qt6CornerE(
    const QMenuBar *self,
    Qt::Corner corner) {
  return self->cornerWidget(corner);
}

//  bool QMenuBar::isNativeMenuBar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMenuBar15isNativeMenuBarEv(const QMenuBar *self) {
  return self->isNativeMenuBar();
}

//  void QMenuBar::setNativeMenuBar(bool nativeMenuBar)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar16setNativeMenuBarEb(
    QMenuBar *self,
    bool nativeMenuBar) {
  self->setNativeMenuBar(nativeMenuBar);
}

//  void QMenuBar::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMenuBar10setVisibleEb(QMenuBar *self, bool visible) {
  self->setVisible(visible);
}
