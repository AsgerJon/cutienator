//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qheaderview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qheaderview.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QHeaderView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QHeaderView10metaObjectEv(
    const QHeaderView *self) {
  return self->metaObject();
}

//  QString QHeaderView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QHeaderView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHeaderView::tr(s, c, n));
}

//  QHeaderView::QHeaderView(Qt::Orientation orientation, QWidget *parent)
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZN11QHeaderViewC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation orientation,
    QWidget *parent) {
  return new QHeaderView(orientation, parent);
}

//  QHeaderView::~QHeaderView()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderViewD1Ev(QHeaderView *self) {
  delete self;
}

//  void QHeaderView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView8setModelEP18QAbstractItemModel(
    QHeaderView *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  Qt::Orientation QHeaderView::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK11QHeaderView11orientationEv(
    const QHeaderView *self) {
  return self->orientation();
}

//  int QHeaderView::offset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView6offsetEv(const QHeaderView *self) {
  return self->offset();
}

//  int QHeaderView::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView6lengthEv(const QHeaderView *self) {
  return self->length();
}

//  QSize QHeaderView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QHeaderView8sizeHintEv(const QHeaderView *self) {
  return new QSize(self->sizeHint());
}

//  void QHeaderView::setVisible(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView10setVisibleEb(QHeaderView *self, bool v) {
  self->setVisible(v);
}

//  int QHeaderView::sectionSizeHint(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView15sectionSizeHintEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->sectionSizeHint(logicalIndex);
}

//  int QHeaderView::visualIndexAt(int position) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView13visualIndexAtEi(
    const QHeaderView *self,
    int position) {
  return self->visualIndexAt(position);
}

//  int QHeaderView::logicalIndexAt(int position) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView14logicalIndexAtEi(
    const QHeaderView *self,
    int position) {
  return self->logicalIndexAt(position);
}

//  int QHeaderView::logicalIndexAt(int x, int y) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView14logicalIndexAtEii(
    const QHeaderView *self,
    int x,
    int y) {
  return self->logicalIndexAt(x, y);
}

//  int QHeaderView::logicalIndexAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView14logicalIndexAtERK6QPoint(
    const QHeaderView *self,
    const QPoint *pos) {
  return self->logicalIndexAt(*pos);
}

//  int QHeaderView::sectionSize(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView11sectionSizeEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->sectionSize(logicalIndex);
}

//  int QHeaderView::sectionPosition(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView15sectionPositionEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->sectionPosition(logicalIndex);
}

//  int QHeaderView::sectionViewportPosition(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView23sectionViewportPositionEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->sectionViewportPosition(logicalIndex);
}

//  void QHeaderView::moveSection(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView11moveSectionEii(
    QHeaderView *self,
    int from,
    int to) {
  self->moveSection(from, to);
}

//  void QHeaderView::swapSections(int first, int second)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView12swapSectionsEii(
    QHeaderView *self,
    int first,
    int second) {
  self->swapSections(first, second);
}

//  void QHeaderView::resizeSection(int logicalIndex, int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView13resizeSectionEii(
    QHeaderView *self,
    int logicalIndex,
    int size) {
  self->resizeSection(logicalIndex, size);
}

//  void QHeaderView::resizeSections(QHeaderView::ResizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView14resizeSectionsENS_10ResizeModeE(
    QHeaderView *self,
    QHeaderView::ResizeMode mode) {
  self->resizeSections(mode);
}

//  bool QHeaderView::isSectionHidden(int logicalIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView15isSectionHiddenEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->isSectionHidden(logicalIndex);
}

//  void QHeaderView::setSectionHidden(int logicalIndex, bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView16setSectionHiddenEib(
    QHeaderView *self,
    int logicalIndex,
    bool hide) {
  self->setSectionHidden(logicalIndex, hide);
}

//  int QHeaderView::hiddenSectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView18hiddenSectionCountEv(const QHeaderView *self) {
  return self->hiddenSectionCount();
}

//  void QHeaderView::hideSection(int logicalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView11hideSectionEi(
    QHeaderView *self,
    int logicalIndex) {
  self->hideSection(logicalIndex);
}

//  void QHeaderView::showSection(int logicalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView11showSectionEi(
    QHeaderView *self,
    int logicalIndex) {
  self->showSection(logicalIndex);
}

//  int QHeaderView::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView5countEv(const QHeaderView *self) {
  return self->count();
}

//  int QHeaderView::visualIndex(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView11visualIndexEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->visualIndex(logicalIndex);
}

//  int QHeaderView::logicalIndex(int visualIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView12logicalIndexEi(
    const QHeaderView *self,
    int visualIndex) {
  return self->logicalIndex(visualIndex);
}

//  void QHeaderView::setSectionsMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView18setSectionsMovableEb(
    QHeaderView *self,
    bool movable) {
  self->setSectionsMovable(movable);
}

//  bool QHeaderView::sectionsMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView15sectionsMovableEv(const QHeaderView *self) {
  return self->sectionsMovable();
}

//  void QHeaderView::setFirstSectionMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView22setFirstSectionMovableEb(
    QHeaderView *self,
    bool movable) {
  self->setFirstSectionMovable(movable);
}

//  bool QHeaderView::isFirstSectionMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView21isFirstSectionMovableEv(
    const QHeaderView *self) {
  return self->isFirstSectionMovable();
}

//  void QHeaderView::setSectionsClickable(bool clickable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView20setSectionsClickableEb(
    QHeaderView *self,
    bool clickable) {
  self->setSectionsClickable(clickable);
}

//  bool QHeaderView::sectionsClickable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView17sectionsClickableEv(const QHeaderView *self) {
  return self->sectionsClickable();
}

//  void QHeaderView::setHighlightSections(bool highlight)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView20setHighlightSectionsEb(
    QHeaderView *self,
    bool highlight) {
  self->setHighlightSections(highlight);
}

//  bool QHeaderView::highlightSections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView17highlightSectionsEv(const QHeaderView *self) {
  return self->highlightSections();
}

//  ResizeMode QHeaderView::sectionResizeMode(int logicalIndex) const
extern "C" Q_DECL_EXPORT
QHeaderView::ResizeMode ritual_ZNK11QHeaderView17sectionResizeModeEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->sectionResizeMode(logicalIndex);
}

//  void QHeaderView::setSectionResizeMode(ResizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView20setSectionResizeModeENS_10ResizeModeE(
    QHeaderView *self,
    QHeaderView::ResizeMode mode) {
  self->setSectionResizeMode(mode);
}

//  void QHeaderView::setSectionResizeMode(int logicalIndex, ResizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView20setSectionResizeModeEiNS_10ResizeModeE(
    QHeaderView *self,
    int logicalIndex,
    QHeaderView::ResizeMode mode) {
  self->setSectionResizeMode(logicalIndex, mode);
}

//  void QHeaderView::setResizeContentsPrecision(int precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView26setResizeContentsPrecisionEi(
    QHeaderView *self,
    int precision) {
  self->setResizeContentsPrecision(precision);
}

//  int QHeaderView::resizeContentsPrecision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView23resizeContentsPrecisionEv(
    const QHeaderView *self) {
  return self->resizeContentsPrecision();
}

//  int QHeaderView::stretchSectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView19stretchSectionCountEv(const QHeaderView *self) {
  return self->stretchSectionCount();
}

//  void QHeaderView::setSortIndicatorShown(bool show)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21setSortIndicatorShownEb(
    QHeaderView *self,
    bool show) {
  self->setSortIndicatorShown(show);
}

//  bool QHeaderView::isSortIndicatorShown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView20isSortIndicatorShownEv(
    const QHeaderView *self) {
  return self->isSortIndicatorShown();
}

//  void QHeaderView::setSortIndicator(int logicalIndex, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView16setSortIndicatorEiN2Qt9SortOrderE(
    QHeaderView *self,
    int logicalIndex,
    Qt::SortOrder order) {
  self->setSortIndicator(logicalIndex, order);
}

//  int QHeaderView::sortIndicatorSection() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView20sortIndicatorSectionEv(
    const QHeaderView *self) {
  return self->sortIndicatorSection();
}

//  Qt::SortOrder QHeaderView::sortIndicatorOrder() const
extern "C" Q_DECL_EXPORT
Qt::SortOrder ritual_ZNK11QHeaderView18sortIndicatorOrderEv(
    const QHeaderView *self) {
  return self->sortIndicatorOrder();
}

//  void QHeaderView::setSortIndicatorClearable(bool clearable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView25setSortIndicatorClearableEb(
    QHeaderView *self,
    bool clearable) {
  self->setSortIndicatorClearable(clearable);
}

//  bool QHeaderView::isSortIndicatorClearable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView24isSortIndicatorClearableEv(
    const QHeaderView *self) {
  return self->isSortIndicatorClearable();
}

//  bool QHeaderView::stretchLastSection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView18stretchLastSectionEv(const QHeaderView *self) {
  return self->stretchLastSection();
}

//  void QHeaderView::setStretchLastSection(bool stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21setStretchLastSectionEb(
    QHeaderView *self,
    bool stretch) {
  self->setStretchLastSection(stretch);
}

//  bool QHeaderView::cascadingSectionResizes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView23cascadingSectionResizesEv(
    const QHeaderView *self) {
  return self->cascadingSectionResizes();
}

//  void QHeaderView::setCascadingSectionResizes(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView26setCascadingSectionResizesEb(
    QHeaderView *self,
    bool enable) {
  self->setCascadingSectionResizes(enable);
}

//  int QHeaderView::defaultSectionSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView18defaultSectionSizeEv(const QHeaderView *self) {
  return self->defaultSectionSize();
}

//  void QHeaderView::setDefaultSectionSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21setDefaultSectionSizeEi(
    QHeaderView *self,
    int size) {
  self->setDefaultSectionSize(size);
}

//  void QHeaderView::resetDefaultSectionSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView23resetDefaultSectionSizeEv(QHeaderView *self) {
  self->resetDefaultSectionSize();
}

//  int QHeaderView::minimumSectionSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView18minimumSectionSizeEv(const QHeaderView *self) {
  return self->minimumSectionSize();
}

//  void QHeaderView::setMinimumSectionSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21setMinimumSectionSizeEi(
    QHeaderView *self,
    int size) {
  self->setMinimumSectionSize(size);
}

//  int QHeaderView::maximumSectionSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView18maximumSectionSizeEv(const QHeaderView *self) {
  return self->maximumSectionSize();
}

//  void QHeaderView::setMaximumSectionSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21setMaximumSectionSizeEi(
    QHeaderView *self,
    int size) {
  self->setMaximumSectionSize(size);
}

//  Qt::Alignment QHeaderView::defaultAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView16defaultAlignmentEv(const QHeaderView *self) {
  return static_cast<int>(self->defaultAlignment().toInt());
}

//  void QHeaderView::setDefaultAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView19setDefaultAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QHeaderView *self,
    int alignment) {
  self->setDefaultAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QHeaderView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView13doItemsLayoutEv(QHeaderView *self) {
  self->doItemsLayout();
}

//  bool QHeaderView::sectionsMoved() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView13sectionsMovedEv(const QHeaderView *self) {
  return self->sectionsMoved();
}

//  bool QHeaderView::sectionsHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView14sectionsHiddenEv(const QHeaderView *self) {
  return self->sectionsHidden();
}

//  QByteArray QHeaderView::saveState() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QHeaderView9saveStateEv(const QHeaderView *self) {
  return new QByteArray(self->saveState());
}

//  bool QHeaderView::restoreState(const QByteArray &state)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QHeaderView12restoreStateERK10QByteArray(
    QHeaderView *self,
    const QByteArray *state) {
  return self->restoreState(*state);
}

//  void QHeaderView::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView5resetEv(QHeaderView *self) {
  self->reset();
}

//  void QHeaderView::setOffset(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView9setOffsetEi(QHeaderView *self, int offset) {
  self->setOffset(offset);
}

//  void QHeaderView::setOffsetToSectionPosition(int visualIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView26setOffsetToSectionPositionEi(
    QHeaderView *self,
    int visualIndex) {
  self->setOffsetToSectionPosition(visualIndex);
}

//  void QHeaderView::setOffsetToLastSection()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView22setOffsetToLastSectionEv(QHeaderView *self) {
  self->setOffsetToLastSection();
}

//  void QHeaderView::headerDataChanged(Qt::Orientation orientation, int
//      logicalFirst, int logicalLast)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView17headerDataChangedEN2Qt11OrientationEii(
    QHeaderView *self,
    Qt::Orientation orientation,
    int logicalFirst,
    int logicalLast) {
  self->headerDataChanged(orientation, logicalFirst, logicalLast);
}
