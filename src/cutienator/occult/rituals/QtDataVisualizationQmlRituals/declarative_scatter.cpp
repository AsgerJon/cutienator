//  Written by hand on 2026-11-25 from
//  QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/
//  declarativescatter_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  The part has no global or exports header of its own (its
//  CMakeLists.txt says NO_GENERATE_CPP_EXPORTS): those of
//  QtDataVisualization, on which it is built, come first.
//  Qt's library offers nothing of this class by name: its class
//  line has no export macro. Written: its virtual functions, called
//  through the object: metaObject(), the destructor, virtual through
//  QObject, and the slots 'handleAxisXChanged',
//  'handleAxisYChanged' and 'handleAxisZChanged', which override
//  those of AbstractDeclarative.
//  Not written: the constructor and 'tr'; the signals; and the
//  functions that are not virtual, which Qt's library offers not,
//  'seriesList' and the static '...SeriesFunc' among them.
#include <QtDataVisualization/qdatavisualizationglobal.h>
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualizationQml/6.12.0/QtDataVisualizationQml/private/declarativescatter_p.h>

//  const QMetaObject *DeclarativeScatter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18DeclarativeScatter10metaObjectEv(
    const DeclarativeScatter *self) {
  return self->metaObject();
}

//  DeclarativeScatter::~DeclarativeScatter()
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeScatterD1Ev(DeclarativeScatter *self) {
  delete self;
}

//  void DeclarativeScatter::handleAxisXChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeScatter18handleAxisXChangedEP15QAbstract3DAxis(
    DeclarativeScatter *self,
    QAbstract3DAxis *axis) {
  self->handleAxisXChanged(axis);
}

//  void DeclarativeScatter::handleAxisYChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeScatter18handleAxisYChangedEP15QAbstract3DAxis(
    DeclarativeScatter *self,
    QAbstract3DAxis *axis) {
  self->handleAxisYChanged(axis);
}

//  void DeclarativeScatter::handleAxisZChanged(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeScatter18handleAxisZChangedEP15QAbstract3DAxis(
    DeclarativeScatter *self,
    QAbstract3DAxis *axis) {
  self->handleAxisZChanged(axis);
}
