//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>

//  QAccessibleTextInterface::~QAccessibleTextInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterfaceD1Ev(
    QAccessibleTextInterface *self) {
  delete self;
}

//  void QAccessibleTextInterface::selection(int selectionIndex, int
//      *startOffset, int *endOffset) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QAccessibleTextInterface9selectionEiPiS0_(
    const QAccessibleTextInterface *self,
    int selectionIndex,
    int *startOffset,
    int *endOffset) {
  self->selection(selectionIndex, startOffset, endOffset);
}

//  int QAccessibleTextInterface::selectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAccessibleTextInterface14selectionCountEv(
    const QAccessibleTextInterface *self) {
  return self->selectionCount();
}

//  void QAccessibleTextInterface::addSelection(int startOffset, int
//      endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterface12addSelectionEii(
    QAccessibleTextInterface *self,
    int startOffset,
    int endOffset) {
  self->addSelection(startOffset, endOffset);
}

//  void QAccessibleTextInterface::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterface15removeSelectionEi(
    QAccessibleTextInterface *self,
    int selectionIndex) {
  self->removeSelection(selectionIndex);
}

//  void QAccessibleTextInterface::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterface12setSelectionEiii(
    QAccessibleTextInterface *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->setSelection(selectionIndex, startOffset, endOffset);
}

//  int QAccessibleTextInterface::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAccessibleTextInterface14cursorPositionEv(
    const QAccessibleTextInterface *self) {
  return self->cursorPosition();
}

//  void QAccessibleTextInterface::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterface17setCursorPositionEi(
    QAccessibleTextInterface *self,
    int position) {
  self->setCursorPosition(position);
}

//  QString QAccessibleTextInterface::text(int startOffset, int endOffset)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleTextInterface4textEii(
    const QAccessibleTextInterface *self,
    int startOffset,
    int endOffset) {
  return new QString(self->text(startOffset, endOffset));
}

//  QString QAccessibleTextInterface::textBeforeOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleTextInterface16textBeforeOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleTextInterface *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textBeforeOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  QString QAccessibleTextInterface::textAfterOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleTextInterface15textAfterOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleTextInterface *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textAfterOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  QString QAccessibleTextInterface::textAtOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleTextInterface12textAtOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleTextInterface *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textAtOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  int QAccessibleTextInterface::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAccessibleTextInterface14characterCountEv(
    const QAccessibleTextInterface *self) {
  return self->characterCount();
}

//  QRect QAccessibleTextInterface::characterRect(int offset) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK24QAccessibleTextInterface13characterRectEi(
    const QAccessibleTextInterface *self,
    int offset) {
  return new QRect(self->characterRect(offset));
}

//  int QAccessibleTextInterface::offsetAtPoint(const QPoint &point) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint(
    const QAccessibleTextInterface *self,
    const QPoint *point) {
  return self->offsetAtPoint(*point);
}

//  void QAccessibleTextInterface::scrollToSubstring(int startIndex, int
//      endIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessibleTextInterface17scrollToSubstringEii(
    QAccessibleTextInterface *self,
    int startIndex,
    int endIndex) {
  self->scrollToSubstring(startIndex, endIndex);
}

//  QString QAccessibleTextInterface::attributes(int offset, int
//      *startOffset, int *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleTextInterface10attributesEiPiS0_(
    const QAccessibleTextInterface *self,
    int offset,
    int *startOffset,
    int *endOffset) {
  return new QString(self->attributes(offset, startOffset, endOffset));
}
