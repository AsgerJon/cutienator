//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/QtGui>
#include <QtGui/qtestsupport_gui.h>
#include <QtGui/qvulkanfunctions.h>
#include <QtGui/qvulkaninstance.h>
#include <QtGui/qvulkanwindow.h>
#include <QtGui/qcolor.h>

//  bool QAccessibleInterface::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QAccessibleInterface7isValidEv(
    const QAccessibleInterface *self) {
  return self->isValid();
}

//  QObject *QAccessibleInterface::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK20QAccessibleInterface6objectEv(
    const QAccessibleInterface *self) {
  return self->object();
}

//  QWindow *QAccessibleInterface::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK20QAccessibleInterface6windowEv(
    const QAccessibleInterface *self) {
  return self->window();
}

//  QAccessibleInterface *QAccessibleInterface::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleInterface10focusChildEv(
    const QAccessibleInterface *self) {
  return self->focusChild();
}

//  QAccessibleInterface *QAccessibleInterface::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleInterface7childAtEii(
    const QAccessibleInterface *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  QAccessibleInterface *QAccessibleInterface::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleInterface6parentEv(
    const QAccessibleInterface *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleInterface::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleInterface5childEi(
    const QAccessibleInterface *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleInterface::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleInterface10childCountEv(
    const QAccessibleInterface *self) {
  return self->childCount();
}

//  int QAccessibleInterface::indexOfChild(const QAccessibleInterface *a0)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleInterface12indexOfChildEPKS_(
    const QAccessibleInterface *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  QString QAccessibleInterface::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAccessibleInterface4textEN11QAccessible4TextE(
    const QAccessibleInterface *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  void QAccessibleInterface::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString(
    QAccessibleInterface *self,
    QAccessible::Text t,
    const QString *text) {
  self->setText(t, *text);
}

//  QRect QAccessibleInterface::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK20QAccessibleInterface4rectEv(
    const QAccessibleInterface *self) {
  return new QRect(self->rect());
}

//  QAccessible::Role QAccessibleInterface::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK20QAccessibleInterface4roleEv(
    const QAccessibleInterface *self) {
  return self->role();
}

//  QAccessible::State QAccessibleInterface::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK20QAccessibleInterface5stateEv(
    const QAccessibleInterface *self) {
  return new QAccessible::State(self->state());
}

//  QColor QAccessibleInterface::foregroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QAccessibleInterface15foregroundColorEv(
    const QAccessibleInterface *self) {
  return new QColor(self->foregroundColor());
}

//  QColor QAccessibleInterface::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QAccessibleInterface15backgroundColorEv(
    const QAccessibleInterface *self) {
  return new QColor(self->backgroundColor());
}

//  QAccessibleTextInterface *QAccessibleInterface::textInterface()
extern "C" Q_DECL_EXPORT
QAccessibleTextInterface *ritual_ZN20QAccessibleInterface13textInterfaceEv(
    QAccessibleInterface *self) {
  return self->textInterface();
}

//  QAccessibleEditableTextInterface
//      *QAccessibleInterface::editableTextInterface()
extern "C" Q_DECL_EXPORT
QAccessibleEditableTextInterface *ritual_ZN20QAccessibleInterface21editableTextInterfaceEv(
    QAccessibleInterface *self) {
  return self->editableTextInterface();
}

//  QAccessibleValueInterface *QAccessibleInterface::valueInterface()
extern "C" Q_DECL_EXPORT
QAccessibleValueInterface *ritual_ZN20QAccessibleInterface14valueInterfaceEv(
    QAccessibleInterface *self) {
  return self->valueInterface();
}

//  QAccessibleActionInterface *QAccessibleInterface::actionInterface()
extern "C" Q_DECL_EXPORT
QAccessibleActionInterface *ritual_ZN20QAccessibleInterface15actionInterfaceEv(
    QAccessibleInterface *self) {
  return self->actionInterface();
}

//  QAccessibleImageInterface *QAccessibleInterface::imageInterface()
extern "C" Q_DECL_EXPORT
QAccessibleImageInterface *ritual_ZN20QAccessibleInterface14imageInterfaceEv(
    QAccessibleInterface *self) {
  return self->imageInterface();
}

//  QAccessibleTableInterface *QAccessibleInterface::tableInterface()
extern "C" Q_DECL_EXPORT
QAccessibleTableInterface *ritual_ZN20QAccessibleInterface14tableInterfaceEv(
    QAccessibleInterface *self) {
  return self->tableInterface();
}

//  QAccessibleTableCellInterface *QAccessibleInterface::tableCellInterface()
extern "C" Q_DECL_EXPORT
QAccessibleTableCellInterface *ritual_ZN20QAccessibleInterface18tableCellInterfaceEv(
    QAccessibleInterface *self) {
  return self->tableCellInterface();
}

//  QAccessibleHyperlinkInterface *QAccessibleInterface::hyperlinkInterface()
extern "C" Q_DECL_EXPORT
QAccessibleHyperlinkInterface *ritual_ZN20QAccessibleInterface18hyperlinkInterfaceEv(
    QAccessibleInterface *self) {
  return self->hyperlinkInterface();
}

//  QAccessibleSelectionInterface *QAccessibleInterface::selectionInterface()
extern "C" Q_DECL_EXPORT
QAccessibleSelectionInterface *ritual_ZN20QAccessibleInterface18selectionInterfaceEv(
    QAccessibleInterface *self) {
  return self->selectionInterface();
}

//  QAccessibleAttributesInterface
//      *QAccessibleInterface::attributesInterface()
extern "C" Q_DECL_EXPORT
QAccessibleAttributesInterface *ritual_ZN20QAccessibleInterface19attributesInterfaceEv(
    QAccessibleInterface *self) {
  return self->attributesInterface();
}

//  QAccessibleViewportInterface *QAccessibleInterface::viewportInterface()
extern "C" Q_DECL_EXPORT
QAccessibleViewportInterface *ritual_ZN20QAccessibleInterface17viewportInterfaceEv(
    QAccessibleInterface *self) {
  return self->viewportInterface();
}
