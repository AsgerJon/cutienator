//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qsplitter.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qsplitter.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QSplitter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QSplitter10metaObjectEv(
    const QSplitter *self) {
  return self->metaObject();
}

//  QString QSplitter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QSplitter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSplitter::tr(s, c, n));
}

//  QSplitter::QSplitter(QWidget *parent)
extern "C" Q_DECL_EXPORT
QSplitter *ritual_ZN9QSplitterC1EP7QWidget(QWidget *parent) {
  return new QSplitter(parent);
}

//  QSplitter::QSplitter(Qt::Orientation a0, QWidget *parent)
extern "C" Q_DECL_EXPORT
QSplitter *ritual_ZN9QSplitterC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation a0,
    QWidget *parent) {
  return new QSplitter(a0, parent);
}

//  QSplitter::~QSplitter()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitterD1Ev(QSplitter *self) {
  delete self;
}

//  void QSplitter::addWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter9addWidgetEP7QWidget(
    QSplitter *self,
    QWidget *widget) {
  self->addWidget(widget);
}

//  void QSplitter::insertWidget(int index, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter12insertWidgetEiP7QWidget(
    QSplitter *self,
    int index,
    QWidget *widget) {
  self->insertWidget(index, widget);
}

//  QWidget *QSplitter::replaceWidget(int index, QWidget *widget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN9QSplitter13replaceWidgetEiP7QWidget(
    QSplitter *self,
    int index,
    QWidget *widget) {
  return self->replaceWidget(index, widget);
}

//  void QSplitter::setOrientation(Qt::Orientation a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter14setOrientationEN2Qt11OrientationE(
    QSplitter *self,
    Qt::Orientation a0) {
  self->setOrientation(a0);
}

//  Qt::Orientation QSplitter::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK9QSplitter11orientationEv(const QSplitter *self) {
  return self->orientation();
}

//  void QSplitter::setChildrenCollapsible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter22setChildrenCollapsibleEb(
    QSplitter *self,
    bool a0) {
  self->setChildrenCollapsible(a0);
}

//  bool QSplitter::childrenCollapsible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSplitter19childrenCollapsibleEv(const QSplitter *self) {
  return self->childrenCollapsible();
}

//  void QSplitter::setCollapsible(int index, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter14setCollapsibleEib(
    QSplitter *self,
    int index,
    bool a1) {
  self->setCollapsible(index, a1);
}

//  bool QSplitter::isCollapsible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSplitter13isCollapsibleEi(
    const QSplitter *self,
    int index) {
  return self->isCollapsible(index);
}

//  void QSplitter::setOpaqueResize(bool opaque)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter15setOpaqueResizeEb(QSplitter *self, bool opaque) {
  self->setOpaqueResize(opaque);
}

//  bool QSplitter::opaqueResize() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSplitter12opaqueResizeEv(const QSplitter *self) {
  return self->opaqueResize();
}

//  void QSplitter::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter7refreshEv(QSplitter *self) {
  self->refresh();
}

//  QSize QSplitter::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QSplitter8sizeHintEv(const QSplitter *self) {
  return new QSize(self->sizeHint());
}

//  QSize QSplitter::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QSplitter15minimumSizeHintEv(const QSplitter *self) {
  return new QSize(self->minimumSizeHint());
}

//  QByteArray QSplitter::saveState() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QSplitter9saveStateEv(const QSplitter *self) {
  return new QByteArray(self->saveState());
}

//  bool QSplitter::restoreState(const QByteArray &state)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSplitter12restoreStateERK10QByteArray(
    QSplitter *self,
    const QByteArray *state) {
  return self->restoreState(*state);
}

//  int QSplitter::handleWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSplitter11handleWidthEv(const QSplitter *self) {
  return self->handleWidth();
}

//  void QSplitter::setHandleWidth(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter14setHandleWidthEi(QSplitter *self, int a0) {
  self->setHandleWidth(a0);
}

//  int QSplitter::indexOf(QWidget *w) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSplitter7indexOfEP7QWidget(
    const QSplitter *self,
    QWidget *w) {
  return self->indexOf(w);
}

//  QWidget *QSplitter::widget(int index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK9QSplitter6widgetEi(const QSplitter *self, int index) {
  return self->widget(index);
}

//  int QSplitter::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSplitter5countEv(const QSplitter *self) {
  return self->count();
}

//  void QSplitter::getRange(int index, int *a1, int *a2) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QSplitter8getRangeEiPiS0_(
    const QSplitter *self,
    int index,
    int *a1,
    int *a2) {
  self->getRange(index, a1, a2);
}

//  QSplitterHandle *QSplitter::handle(int index) const
extern "C" Q_DECL_EXPORT
QSplitterHandle *ritual_ZNK9QSplitter6handleEi(
    const QSplitter *self,
    int index) {
  return self->handle(index);
}

//  void QSplitter::setStretchFactor(int index, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSplitter16setStretchFactorEii(
    QSplitter *self,
    int index,
    int stretch) {
  self->setStretchFactor(index, stretch);
}
