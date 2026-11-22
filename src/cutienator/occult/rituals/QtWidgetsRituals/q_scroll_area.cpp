//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qscrollarea.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qscrollarea.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QScrollArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QScrollArea10metaObjectEv(
    const QScrollArea *self) {
  return self->metaObject();
}

//  QString QScrollArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QScrollArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScrollArea::tr(s, c, n));
}

//  QScrollArea::QScrollArea(QWidget *parent)
extern "C" Q_DECL_EXPORT
QScrollArea *ritual_ZN11QScrollAreaC1EP7QWidget(QWidget *parent) {
  return new QScrollArea(parent);
}

//  QScrollArea::~QScrollArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollAreaD1Ev(QScrollArea *self) {
  delete self;
}

//  QWidget *QScrollArea::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QScrollArea6widgetEv(const QScrollArea *self) {
  return self->widget();
}

//  void QScrollArea::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollArea9setWidgetEP7QWidget(
    QScrollArea *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QScrollArea::takeWidget()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN11QScrollArea10takeWidgetEv(QScrollArea *self) {
  return self->takeWidget();
}

//  bool QScrollArea::widgetResizable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QScrollArea15widgetResizableEv(const QScrollArea *self) {
  return self->widgetResizable();
}

//  void QScrollArea::setWidgetResizable(bool resizable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollArea18setWidgetResizableEb(
    QScrollArea *self,
    bool resizable) {
  self->setWidgetResizable(resizable);
}

//  QSize QScrollArea::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QScrollArea8sizeHintEv(const QScrollArea *self) {
  return new QSize(self->sizeHint());
}

//  bool QScrollArea::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QScrollArea18focusNextPrevChildEb(
    QScrollArea *self,
    bool next) {
  return self->focusNextPrevChild(next);
}

//  Qt::Alignment QScrollArea::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QScrollArea9alignmentEv(const QScrollArea *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QScrollArea::setAlignment(Qt::Alignment a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollArea12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QScrollArea *self,
    int a0) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(a0));
}

//  void QScrollArea::ensureVisible(int x, int y, int xmargin, int ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollArea13ensureVisibleEiiii(
    QScrollArea *self,
    int x,
    int y,
    int xmargin,
    int ymargin) {
  self->ensureVisible(x, y, xmargin, ymargin);
}

//  void QScrollArea::ensureWidgetVisible(QWidget *childWidget, int xmargin,
//      int ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollArea19ensureWidgetVisibleEP7QWidgetii(
    QScrollArea *self,
    QWidget *childWidget,
    int xmargin,
    int ymargin) {
  self->ensureWidgetVisible(childWidget, xmargin, ymargin);
}
